import streamlit as st

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://t4.ftcdn.net/jpg/01/23/73/15/360_F_123731572_KMfBEkpbRlfQj1ypdPVwv4W0r27B9hVJ.jpg");
  background-size: cover;
}
[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}

</style>
"""
st.markdown(page_element, unsafe_allow_html=True)

# Configuration and Utility Imports (Need to redefine constants and utility functions used ONLY by this page)

DASHBOARD_NAME = "👨‍🍳 Chef's Compass"
USER_GMAIL = "shreerajpatil98@gmail.mail.com"
USER_LINKEDIN_URL = "https://www.linkedin.com/in/shreeraj-patil-142011136?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
DATASET_LINK = "https://www.kaggle.com/datasets/prashantsingh001/recipes-dataset-64k-dishes" 

def generate_qr_code_html(data_to_encode, label, qr_color='000000'): 
    """Generates and displays a colorful QR code (scannable)."""
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={data_to_encode}&color={qr_color}"
    
    html_content = f"""
    <div style="text-align: center; margin-bottom: 20px; border: 1px solid #ccc; padding: 15px; border-radius: 8px; background-color: white;">
        <p style="font-size: large; font-weight: bold; margin-bottom: 10px; color: #5D5D81;">{label}</p>
        <p style="font-size: small; color: #333; margin-bottom: 10px;">Scan Code:</p>
        <img src="{qr_code_url}" alt="QR code for {label}" style="width:150px; height:150px; display: block; margin: auto;">
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)


def page_about_us():
    """Displays the About Us page content."""
    st.header("About Us ℹ️")
    st.markdown("---")
    
    st.subheader("Dashboard Details")
    # NOTE: The f-string is used here. LaTeX curly braces must be escaped with double braces {{}}
    st.markdown(f"""
        **{DASHBOARD_NAME}** is an interactive recipe finder built on Streamlit. 
        It helps you discover recipes based on ingredients you have, applying a flexible match threshold. 
        Recipes are conveniently sorted from **Simple** to **Complex** for ease of use.
        
        ---
        
        **Raw Dataset Source**
        
        [Recipes Dataset : 64k Dishes]({DATASET_LINK})
        
        ---
        
        **Target Users and Core Objective** 🎯
        
        * **Key Users:** The **Home Cook** & the **Meal Planner**, who are busy professionals needing to maximize the use of existing ingredients to save on grocery bills.
        * **Core Goal:** Instant recipe rankings that **maximize existing ingredients** and **minimize guesswork**.
        
        **Key Performance Indicators (KPIs)** 📊
        
        The dashboard uses these metrics to provide actionable insights:
        
        1.  **Ingredient Match Score:** A normalized score showing the percentage of a recipe's required ingredients that the user currently has.
            
            Match Score= # of ingredients matched/num_ingredients in recipe X 100
            
            *Purpose:* Ranks recipes so users see the best possible dishes first.
        
        2.  **Number of Possible Recipes:** The count of all recipes that can be made with the given ingredients (either full match or partial match above a set threshold).
            
            *Purpose:* Shows the user how many options they have based on what’s available in their kitchen.
        
        3.  **Average Recipe Complexity:** Measures how complex the suggested recipes are, derived from dataset fields.
            
            Complexity = (num_ingredients + num_steps)/2
            
            *Purpose:* Lets the user filter for quick & simple vs. detailed & involved dishes.
        
        **Future Engineering & Data Preparation** 🛠️
        
        * **Ingredient Cleaning:** We performed vigorous cleaning on the ingredients column to create a separate, normalized list of ingredients for accurate matching.
        * **Ingredient Clustering:** Different types of ingredients (e.g., 'green onion', 'scallion', 'onion powder') have been **clustered** into a single category (e.g., 'onion') for simple, effective matching. This removes friction for the user.
        * **Duplicate Removal:** Duplicated recipes were removed from the dataset to ensure an effortless user experience.
        
        **How to use the Dashboard** 💡
        
        * **Recipe Explorer Tab:**
            * **Filter by Category:** Filter options like "Desserts," "Indian," "Fruit salads," etc.
            * **Select Ingredients:** User inputs the names of the ingredients they currently have.
            * **Ingredients Match Threshold (%):** Used to see either a full match or partial match. Setting this to **100%** shows only recipes where *all* required ingredients match the user's input.
        * **Favorites Page:** User can add and manage their favorite recipes by clicking on the **"Add to favorites"** button on the Recipe Explorer page.
        
        ---
        
        **Contact & Connect**
        
        Scan the colorful QR codes below to retrieve the contact details.
    """)

    col1, col2 = st.columns(2)
    
    with col1:
        generate_qr_code_html(USER_GMAIL, "Gmail ID", qr_color='EA4335')

    with col2:
        generate_qr_code_html(USER_LINKEDIN_URL, "LinkedIn ID", qr_color='0A66C2')
    st.markdown("---")


# Execution for the multi-page app
if __name__ == '__main__':
    page_about_us()

