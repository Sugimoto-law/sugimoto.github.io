from bs4 import BeautifulSoup
import os

# Define the directory where your HTML files are located
html_files_dir = '.'

# Define the new value for the "rel" attribute


# Function to process HTML files in a directory and its subdirectories
def process_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.html'):
                file_path = os.path.join(root, filename)

                # Open the HTML file
                with open(file_path, 'r') as file:
                    html_content = file.read()

                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(html_content, 'html.parser')

                # Find all <link> tags
                link_tags = soup.find_all('link')
                
                log_file_str =""
                
                for link_tags in link_tags:
                    # Iterate through the <link> tags and update the "rel" attribute
                    if link_tags["rel"] == ["canonical"]:
                        
                        #add before and after to log_file_str
                        #change href to current value + ".html"
                        print("before:" + link_tags["href"])
                        log_file_str += "before:" + link_tags["href"] + "\n"
                        link_tags["href"] = link_tags["href"] + ".html"
                        print("after:" + link_tags["href"])
                        log_file_str += "after:" + link_tags["href"] + "\n"

                # Save the modified HTML content back to the file
                with open(file_path, 'w') as file:
                    file.write(str(soup))
                    
                with open("log_file.txt", 'a') as file:
                    file.write(log_file_str)

                print(f"Updated <link> tags in {file_path}")

# Start processing HTML files in the specified directory and its subdirectories
process_html_files(html_files_dir)

print("All HTML files processed.")