from happytransformer import HappyTextToText, TTTrainArgs
import os

# 1. Change the model to 'google/flan-t5-small'
model_type = "T5"
model_name = "google/flan-t5-small" 

happy_tt = HappyTextToText(model_type, model_name)

# 2. Increase training intensity for a smaller model and tiny dataset
args = TTTrainArgs(
    num_train_epochs=50,    
    batch_size=1, 
    learning_rate=1e-4      
)

# 3. Train
happy_tt.train("tr.csv", args=args)

# 4. Save to your local folder
current_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(current_dir, "my_custom_model")
happy_tt.save(save_path)

print(f"Success! Smaller model saved to {save_path}")