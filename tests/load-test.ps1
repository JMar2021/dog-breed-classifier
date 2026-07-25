while ($true) {
    curl.exe `
      -X POST `
      http://localhost:8000/predict `
      -F "file=@.\images\samples\retriever1.jpg"

    Start-Sleep -Milliseconds 100
}