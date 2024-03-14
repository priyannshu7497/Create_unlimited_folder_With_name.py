import os
import time

# Function to create folders
def create_folders():
    # Create a directory if it doesn't exist
    if not os.path.exists("folders"):
        os.makedirs("folders")
    
    # Change directory to the newly created folder
    os.chdir("folders")
    
    # Create 100 folders with custom names
    for i in range(1, 1001): # you can change the value create a more folder just chnage the value
        folder_name = f"new_{i:03}"  # Customize folder names here
        os.makedirs(folder_name)

# Measure the time taken
start_time = time.time()

# Call the function to create folders
create_folders()

# Calculate elapsed time
elapsed_time = time.time() - start_time
print(f"Folders created in {elapsed_time:.2f} seconds.")
