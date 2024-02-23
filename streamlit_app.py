import streamlit as st
import os
import markdown

# Mock function to list topics and their paths
def list_topics(base_path):
    return {
        "Python": os.path.join(base_path, "Python"),
        "Django": os.path.join(base_path, "Django")
    }

# Mock function to list categories for a given topic
def list_categories(topic_path):
    return [d for d in os.listdir(topic_path) if os.path.isdir(os.path.join(topic_path, d))]

# Mock function to list modules for a given category
def list_modules(category_path):
    return sorted([f for f in os.listdir(category_path) if os.path.isdir(os.path.join(category_path, f))], key=lambda x: int(x.split('_')[0]))

# Mock function to list markdown files for a given module
def list_md_files(module_path):
    return sorted([f for f in os.listdir(module_path) if f.endswith('.md')], key=lambda x: int(x.split('_')[0]))

# Function to read and return markdown content
def get_md_content(md_file_path):
    with open(md_file_path, 'r') as file:
        return file.read()

# Assuming a base path for demonstration; replace this with your actual path or GitHub URL structure
base_path = "Learning"

# Main Streamlit app
def main():
    st.title("Welcome to Learning Topics")

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
                    md_html = markdown.markdown(md_content)
                    st.markdown(md_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
