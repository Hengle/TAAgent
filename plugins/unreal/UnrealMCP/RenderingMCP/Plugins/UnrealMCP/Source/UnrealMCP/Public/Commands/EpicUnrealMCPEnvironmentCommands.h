#pragma once

#include "CoreMinimal.h"
#include "Json.h"

/**
 * Environment, Lighting and Viewport Commands
 */
class FEpicUnrealMCPEnvironmentCommands
{
public:
    // Main command dispatcher
    TSharedPtr<FJsonObject> HandleCommand(const FString& CommandType, const TSharedPtr<FJsonObject>& Params);
    
    // Viewport screenshot
    TSharedPtr<FJsonObject> HandleGetViewportScreenshot(const TSharedPtr<FJsonObject>& Params);
    
    // Light management
    TSharedPtr<FJsonObject> HandleCreateLight(const TSharedPtr<FJsonObject>& Params);
    TSharedPtr<FJsonObject> HandleSetLightProperties(const TSharedPtr<FJsonObject>& Params);
    TSharedPtr<FJsonObject> HandleGetLights(const TSharedPtr<FJsonObject>& Params);
    TSharedPtr<FJsonObject> HandleDeleteLight(const TSharedPtr<FJsonObject>& Params);
    
    // Post Process Volume
    TSharedPtr<FJsonObject> HandleCreatePostProcessVolume(const TSharedPtr<FJsonObject>& Params);
    TSharedPtr<FJsonObject> HandleSetPostProcessSettings(const TSharedPtr<FJsonObject>& Params);
    
    // Actor spawning and material assignment
    TSharedPtr<FJsonObject> HandleSpawnBasicActor(const TSharedPtr<FJsonObject>& Params);
    TSharedPtr<FJsonObject> HandleSetActorMaterial(const TSharedPtr<FJsonObject>& Params);
};
