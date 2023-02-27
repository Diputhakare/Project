from mushroom.pipeline.training_pipeline import start_training_pipeline


file_path="/config/workspace/mushroom.csv"
print(__name__)
if __name__=="__main__":
     try:
          #start_training_pipeline()
          output_file = start_training_pipeline()
          print(output_file)
     except Exception as e:
          print(e)