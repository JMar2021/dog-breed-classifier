param(
    [Parameter(Mandatory=$true)]
    [string]$ImageTag,

    [string]$Environment="dev"
)

$image = "ghcr.io/jmar2021/dog-breed-classifier:$ImageTag"

Write-Host "Deploying $image"
Write-Host "Deploying environment: $Environment"


$valuesFile = "./dog-classifier/values-$Environment.yaml"

Write-Host "Using values: $valuesFile"


helm upgrade dog-classifier ./dog-classifier `
    --namespace dog-classifier `
    --values $valuesFile `
    --set image.tag=$ImageTag `
    --install

if ($LASTEXITCODE -ne 0) {
    Write-Host "Failed to upgrade Helm release"
    exit 1
}


Write-Host "Waiting for rollout..."

kubectl rollout status deployment/classifier-api `
    -n dog-classifier `
    --timeout=120s

if ($LASTEXITCODE -ne 0) {

    Write-Host "Deployment failed. Rolling back Helm release..."

    helm rollback dog-classifier `
        -n dog-classifier

    Write-Host "Rollback complete"
    exit 1
}


Write-Host "Rollout complete. Checking application health..."


$healthUrl = "http://classifier.local/health"

try {

    $response = Invoke-RestMethod $healthUrl -TimeoutSec 10

    Write-Host "Health check passed:"
    Write-Host $response

}
catch {

    Write-Host "Health check failed. Rolling back Helm release..."

    helm rollback dog-classifier `
        -n dog-classifier

    exit 1
}


Write-Host "Deployment successful!"