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
    static TSharedPtr<FJsonObject> HandleCommand(const FString& CommandType, const TSharedPtr<FJsonObject>& Params);
    
    // Viewport screenshot
    static TSharedPtr<FJsonObject> HandleGetViewportScreenshot(const TSharedPtr<FJsonObject>& Params);
    
    // Light management
    static TSharedPtr<FJsonObject> HandleCreateLight(const TSharedPtr<FJsonObject>& Params);
    static TSharedPtr<FJsonObject> HandleSetLightProperties(const TSharedPtr<FJsonObject>& Params);
    static TSharedPtr<FJsonObject> HandleGetLights(const TSharedPtr<FJsonObject>& Params);
    static TSharedPtr<FJsonObject> HandleDeleteLight(const TSharedPtr<FJsonObject>& Params);
    
    // Post Process Volume
    static TSharedPtr<FJsonObject> HandleCreatePostProcessVolume(const TSharedPtr<FJsonObject>& Params);
    static TSharedPtr<FJsonObject> HandleSetPostProcessSettings(const TSharedPtr<FJsonObject>& Params);
    
    // Actor spawning and material assignment
    static TSharedPtr<FJsonObject> HandleSpawnBasicActor(const TSharedPtr<FJsonObject>& Params);
    static TSharedPtr<FJsonObject> HandleSetActorMaterial(const TSharedPtr<FJsonObject>& Params);
};
