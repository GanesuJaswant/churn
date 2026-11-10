# Temporary registry management helper script
import mlflow
from mlflow.tracking import MlflowClient

def inspect_registry():
    client = MlflowClient()
    print("Registered models:")
    for rm in client.search_registered_models():
        print(f"- Name: {rm.name}")
        for mv in rm.latest_versions:
            print(f"  Version: {mv.version}, Stage: {mv.current_stage}, Status: {mv.status}")

if __name__ == "__main__":
    inspect_registry()
