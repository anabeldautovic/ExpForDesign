import os
import subprocess

# Define the parameters to iterate over
n_topics_values = [20, 50, 100, 200]
alpha_word_values = [0.2, 0.3, 0.4, 0.5]

# Paths (update these with your actual paths)
path_to_save_results = "/workspace/ptm/data_preprocessing/results_itunes/alphaent04"
wikipedia2vec_embeddings_file = "/workspace/ptm/data_preprocessing/wiki2vec_pretrained/enwiki_20180420_300d.pkl"
output_base_dir = "/workspace/ptm/neice_model/output_itunes/alphaent04"
mask_entities_file = "/workspace/ptm/data_preprocessing/results_itunes/alphaent04/mask_enrich_entities_th0.40_k500.npz"
vocab_file = "/workspace/ptm/data_preprocessing/results_itunes/alphaent04/new_vocab_th0.40_k500.txt"

# Loop over all combinations of parameters
for n_topics in n_topics_values:
    for alpha_word in alpha_word_values:
        # Create a unique output folder name
        output_dir = os.path.join(output_base_dir, f"topics_{n_topics}_alpha_{alpha_word}")
        os.makedirs(output_dir, exist_ok=True)

        # Build the command
        command = [
            "python", "main.py",
            "--corpus", os.path.join(path_to_save_results, "prepro_enrich_entities_th0.40_k500.txt"),
            "--embeddings", wikipedia2vec_embeddings_file,
            "--output_dir", output_dir,
            "--mask_entities_file", mask_entities_file,
            "--vocab", vocab_file,
            "--n_topics", str(n_topics),
            "--n_neighbours", "500",
            "--alpha_word", str(alpha_word),
            "--alpha_nmf", "0.1",
            "--NED"
        ]

        # Print the command for debugging
        print("Running command:", " ".join(command))

        # Run the command
        try:
            subprocess.run(command, check=True)
            print(f"Experiment with n_topics={n_topics}, alpha_word={alpha_word} completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Experiment with n_topics={n_topics}, alpha_word={alpha_word} failed. Error: {e}")
