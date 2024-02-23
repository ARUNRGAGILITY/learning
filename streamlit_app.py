import streamlit as st
import os
import re

def display_breadcrumbs(selected_topic, selected_category, selected_module, selected_md_file):
    # Initialize the breadcrumb with the home link
    breadcrumbs = "Home"
    
    # Dynamically add to the breadcrumb based on what the user has selected
    if selected_topic:
        breadcrumbs += f" > {selected_topic}"
    if selected_category:
        breadcrumbs += f" > {selected_category}"
    if selected_module:
        breadcrumbs += f" > {selected_module}"
    if selected_md_file:
        breadcrumbs += f" > {selected_md_file}"

    # Display the breadcrumbs at the top of the main content area
    st.markdown(f"#### {breadcrumbs}")


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
        
        # Place the radio button in the sidebar for display options
        display_option = st.sidebar.radio(
            "Display:",
            ['All Content', 'Code Only', 'Concepts Only'],
            key="display_option_sidebar"  # Ensuring unique key for sidebar widgets
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

def main():
    st.sidebar.title("Learning Topics")

    base_path = "Learning"  # Assuming a base path for demonstration
    
    topics = list_topics(base_path)
    selected_topic = st.sidebar.selectbox("Select a Topic", options=["Select a Topic"] + list(topics.keys()))
    
    selected_category = None
    selected_module = None
    selected_md_file = None

    if selected_topic != "Select a Topic":
        topic_path = topics[selected_topic]
        categories = list_categories(topic_path)
        selected_category = st.sidebar.selectbox("Select a Category", options=["Select a Category"] + categories)

        if selected_category != "Select a Category":
            category_path = os.path.join(topic_path, selected_category)
            modules = list_modules(category_path)
            selected_module = st.sidebar.selectbox("Select a Module", options=["Select a Module"] + modules)

            if selected_module != "Select a Module":
                module_path = os.path.join(category_path, selected_module)
                md_files = list_md_files(module_path)
                selected_md_file = st.sidebar.selectbox("Select a Sub-Topic", options=["Select a Sub-Topic"] + md_files)

    # Display breadcrumbs
    display_breadcrumbs(selected_topic, selected_category, selected_module, selected_md_file)

    # Now display the content based on the selected_md_file as previously defined
    if selected_md_file and selected_md_file != "Select a Sub-Topic":
        md_file_path = os.path.join(module_path, selected_md_file)
        display_filtered_content(md_file_path)

if __name__ == "__main__":
    main()
