import os
import subprocess

# Paths (update these with your actual paths)
output_base_dir = "/workspace/ptm/neice_model/output_itunes/alphaent04"  # Base directory containing output folders
wikipedia_db_path = "/workspace/ptm/evaluation/wikipedia_bd"   # Path to the Wikipedia DB for evaluation
number_top_words = 10                         # Number of top words to consider for evaluation
evaluation_script = "./evaluate-topics.sh"    # Path to the evaluation script
results_file = "/workspace/ptm/evaluation/results_itunes_alpha_ent_04.txt"  # File to save results
alpha_ent = 0.4                               # Current value of alpha_ent being used

# Prepare results file
with open(results_file, "w") as f:
    # Write the header
    f.write("Evaluation Results (alpha_ent={})\n".format(alpha_ent))
    f.write("========================================\n")
    f.write("n_topics\talpha_word\tCV_Score\n")

# Iterate over all output folders
for folder_name in os.listdir(output_base_dir):
    folder_path = os.path.join(output_base_dir, folder_name)

    # Ensure it's a directory and contains the required file
    if os.path.isdir(folder_path):
        topics_model_file = os.path.join(folder_path, "top_words.txt")
        if os.path.exists(topics_model_file):
            # Extract parameter values from folder name (assumes consistent naming)
            try:
                # Assuming folder name format: "topics_<n_topics>_alpha_<alpha_word>"
                parts = folder_name.split("_")
                n_topics = int(parts[1])
                alpha_word = float(parts[3])
            except (IndexError, ValueError):
                print("Unexpected folder naming convention: {}. Skipping...".format(folder_name))
                continue

            # Build the command
            command = [
                evaluation_script,
                topics_model_file,
                str(number_top_words),
                wikipedia_db_path
            ]

            # Run the command and capture the output
            try:
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

                if process.returncode == 0:
                    # Extract the CV score from the output (assumes it's printed to stdout)
                    cv_score = stdout.strip().decode('utf-8')  # Modify if output format differs
                    print("Evaluation completed for {}. CV Score: {}".format(folder_name, cv_score))

                    # Save to results file
                    with open(results_file, "a") as f:
                        f.write("{}\t{}\t{}\n".format(n_topics, alpha_word, cv_score))
                else:
                    print("Evaluation failed for {}. Error:\n{}".format(folder_name, stderr.decode('utf-8')))

            except Exception as e:
                print("Error occurred while processing {}: {}".format(folder_name, e))
        else:
            print("Missing 'top_words.txt' in {}. Skipping...".format(folder_name))