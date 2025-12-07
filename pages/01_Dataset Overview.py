import streamlit as st
import pandas as pd

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://www.shutterstock.com/image-photo/food-background-spices-herbs-utensil-260nw-2254302831.jpg");
  background-size: cover;
}
[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}

</style>
"""
st.markdown(page_element, unsafe_allow_html=True)


def convert_df_to_csv(df):
    """Converts the DataFrame to a CSV string for download."""
    return df.to_csv(index=False).encode('utf-8')

# The page function from the original file
def page_overview(df):
    """Displays an overview of the dataset and allows full data download."""
    st.header("Recipe Dataset Overview 📚")
    st.markdown("---")
    st.markdown("""
        This dashboard provides an interactive way to explore and filter a large dataset of recipes.
        You can search for recipes based on the ingredients you have and save your favorites!
    """)
    st.subheader("Dataset Summary")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Recipes", f"{len(df):,}")
    # Use st.session_state for ingredients count
    col2.metric("Total Ingredients", f"{len(st.session_state.all_ingredients):,}")
    col3.metric("Average Steps", f"{df['num_steps'].mean():.1f}")
    
    st.subheader("Data Columns Preview")
    
    preview_cols = ['recipe_title', 'category', 'num_ingredients', 'num_steps', 'Complexity', 'cleaned_ingredients_filtered']
    df_preview = df[preview_cols].head() 

    st.dataframe(df_preview, use_container_width=True)
    
    csv_full = convert_df_to_csv(df)

    st.download_button(
        label="Download Full Recipe Dataset (CSV)",
        data=csv_full,
        file_name='64k_dishes_full_dataset.csv',
        mime='text/csv',
        type="primary"
    )

    with st.expander("Detailed Data Information"):
        st.write(f"The dataset contains **{len(df)}** recipes across **{df['category'].nunique()}** categories.")
        st.write("Key columns used for the dashboard:")
        st.markdown("""
        * **Recipe Title**: The name of the recipe.
        * **Cleaned Ingredients Filtered**: A cleaned, comma-separated list of ingredients, used for filtering.
        * **Directions**: The steps to make the recipe.
        * **Num Steps**: The total number of steps in the recipe, used to calculate **Complexity**.
        * **Complexity**: Categorized as Simple ($\le$ Q1 steps), Medium ($\le$ Q3 steps), or Complex ($>$ Q3 steps).
        """)
    st.markdown("---")

# Execution for the multi-page app
if __name__ == '__main__':
    if 'data' in st.session_state:
        page_overview(st.session_state.data)
    else:
        st.error("Data not loaded. Please ensure the main `app.py` runs successfully.")

