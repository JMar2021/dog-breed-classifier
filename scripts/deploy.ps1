param(
    [Parameter(Mandatory=$true)]
    [string]$ImageTag
)

$image = "ghcr.io/jmar2021/dog-breed-classifier:$ImageTag"

Write-Host "Deploying $image"

kubectl set image deployment/classifier-api `
    classifier-api=$image `
    -n dog-classifier

kubectl rollout status deployment/classifier-api `
    -n dog-classifier