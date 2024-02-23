import streamlit as st
import os
import re

def parse_markdown_content(markdown_content):
    """
    Parses the Markdown content to separate code, concepts, and other content.
    
    Parameters:
    - markdown_content: str, the full content of the Markdown file.
    
    Returns:
    - dict, containing separated 'code', 'concepts', and 'all' content.
    """
    code_blocks = re.findall(r'```.*?```', markdown_content, re.DOTALL)
    # Regex to match code blocks
    code_blocks = re.findall(r'```.*?```', markdown_content, re.DOTALL)
    # Updated regex for concept blocks to ensure it captures multiple instances
    concept_blocks = re.findall(r'<!--concept-->\s*(.*?)\s*<!--end-->', markdown_content, re.DOTALL)

    # Join all code blocks with a newline
    code_only = '\n'.join(code_blocks)
    # Join all concept blocks with a newline
    concepts_only = '\n\n'.join(concept_blocks)
    
    return {'code': code_only, 'concepts': concepts_only, 'all': markdown_content}



def display_filtered_content(selected_file_path):
    """
    Displays the content of the selected Markdown file based on user's choice of filtering.
    
    Parameters:
    - selected_file_path: str, path to the selected Markdown file.
    """
    
    
    if selected_file_path:
        with open(selected_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        parsed_content = parse_markdown_content(content)
        
        # Inject custom CSS with st.markdown
        st.markdown("""
        <style>
        /* Targeting the radio buttons directly for horizontal layout */
        div.stRadio > div[role="radiogroup"] > label {
        display: inline-block; /* Make radio items inline */
        margin-right: 10px; /* Spacing between options */
        }
        /* Adjusting font size */
        div.stRadio > div[role="radiogroup"] > label > div:first-child {
        font-size: 0.8rem; /* Smaller font size */
        }
        </style>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns([3, 1])  # Adjust as needed

        with col2:
            display_option = st.radio(
                "Display:",
                ['All Content', 'Code Only', 'Concepts Only'],
                key="display_option"  # Ensure unique key if necessary
            )    

        # Filter content based on the selected option
        if display_option == 'Code Only':
            st.markdown(parsed_content['code'], unsafe_allow_html=True)
        elif display_option == 'Concepts Only':
            st.markdown(parsed_content['concepts'], unsafe_allow_html=True)
        else:  # All Content
            st.markdown(parsed_content['all'], unsafe_allow_html=True)



# Mock function to list topics and their paths
def list_topics(base_path):
    topics = {}
    for name in os.listdir(base_path):
        path = os.path.join(base_path, name)
        if os.path.isdir(path):
            topics[name] = path
    return topics

def sort_key(name):
    # Attempt to split the name into parts and convert each to int if possible
    parts = name.split('_')[0].split('.')
    sorted_parts = []
    for part in parts:
        try:
            # Convert number-like parts to integers
            sorted_parts.append(int(part))
        except ValueError:
            # Leave non-integer parts as is
            sorted_parts.append(part)
    return tuple(sorted_parts)

# Adjust the list_modules function to use this new sort_key
def list_modules(category_path):
    return sorted(
        [f for f in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, f))],
        key=sort_key
    )

# Adjust the list_md_files function similarly if needed
def list_md_files(module_path):
    return sorted(
        [f for f in os.listdir(module_path) if f.endswith('.md')],
        key=sort_key
    )

# Mock function to list categories for a given topic
def list_categories(topic_path):
    return [d for d in os.listdir(topic_path) if os.path.isdir(os.path.join(topic_path, d))]



# Function to read and return markdown content
def get_md_content(md_file_path):
    with open(md_file_path, 'r') as file:
        return file.read()

# Main Streamlit app
def main():
    st.title("Welcome to Learning Topics")

    # Assuming a base path for demonstration; replace this with your actual path or GitHub URL structure
    base_path = "Learning"
    
    topics = list_topics(base_path)
    selected_topic = st.sidebar.selectbox("Select a Topic", options=list(topics.keys()))

    if selected_topic:
        topic_path = topics[selected_topic]
        categories = list_categories(topic_path)
        selected_category = st.sidebar.selectbox("Select a Category", options=categories)

        if selected_category:
            category_path = os.path.join(topic_path, selected_category)
            modules = list_modules(category_path)
            selected_module = st.sidebar.selectbox("Select a Module", options=modules)

            if selected_module:
                module_path = os.path.join(category_path, selected_module)
                md_files = list_md_files(module_path)
                selected_md_file = st.sidebar.selectbox("Select a Sub-Topic", options=md_files)

                if selected_md_file:
                    md_file_path = os.path.join(module_path, selected_md_file)
                    display_filtered_content(md_file_path)

if __name__ == "__main__":
    main()
