import streamlit as st
import os

# Mock function to list topics and their paths
def list_topics(base_path):
    return {
        "Python": os.path.join(base_path, "Python"),
        "Django": os.path.join(base_path, "Django")
    }
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
                    md_content = get_md_content(md_file_path)
                    st.markdown(md_content)

if __name__ == "__main__":
    main()
