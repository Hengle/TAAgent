$UBT_PATH = "E:\UE\UE_5.7\Engine\Binaries\DotNET\UnrealBuildTool\UnrealBuildTool.exe"
$PROJECT_PATH = "d:\CodeBuddy\rendering-mcp\plugins\unreal\UnrealMCP\RenderingMCP\RenderingMCP.uproject"
$PLUGIN_PATH = "d:\CodeBuddy\rendering-mcp\plugins\unreal\UnrealMCP\RenderingMCP\Plugins\UnrealMCP\UnrealMCP.uplugin"
$LOG_DIR = "d:\CodeBuddy\rendering-mcp\build_logs"
$TIMESTAMP = Get-Date -Format "yyyyMMdd_HHmmss"
$LOG_FILE = Join-Path $LOG_DIR "build_$TIMESTAMP.log"

# Create log directory if not exists
if (-not (Test-Path $LOG_DIR)) {
    New-Item -ItemType Directory -Path $LOG_DIR | Out-Null
}

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Build started at $(Get-Date)" -ForegroundColor Cyan
Write-Host "Log file: $LOG_FILE" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

# Run build and capture output
$arguments = @(
    "RenderingMCPEditor",
    "Win64",
    "Development",
    "-Project=`"$PROJECT_PATH`"",
    "-Plugin=`"$PLUGIN_PATH`""
)

$output = & $UBT_PATH $arguments 2>&1

# Save to log file
$output | Out-File -FilePath $LOG_FILE -Encoding UTF8

# Display output
$output | ForEach-Object { Write-Host $_ }

$buildExitCode = $LASTEXITCODE

Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Build finished at $(Get-Date)" -ForegroundColor Cyan
Write-Host "Exit code: $buildExitCode" -ForegroundColor $(if ($buildExitCode -eq 0) { "Green" } else { "Red" })
Write-Host "Log saved to: $LOG_FILE" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan

# Parse and display errors if any
if ($buildExitCode -ne 0) {
    Write-Host ""
    Write-Host "========== ERRORS FOUND ==========" -ForegroundColor Red
    $errors = $output | Select-String -Pattern "error|Error:|fatal" -CaseSensitive:$false
    if ($errors) {
        $errors | ForEach-Object { Write-Host $_.Line -ForegroundColor Red }
    } else {
        Write-Host "Check log file for details" -ForegroundColor Yellow
    }
    Write-Host ""
}

exit $buildExitCode
