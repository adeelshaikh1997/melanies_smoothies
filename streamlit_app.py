import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f"Customize your Smoothie! :cup_with_straw: {st.__version__}")
st.write(
  """Replace this example with your own code!
  **And if you're new to Streamlit,** check
  out our easy-to-follow guides at
  [docs.streamlit.io](https://docs.streamlit.io).
  """
)


name_on_order = st.text_input("Name on Smoothie:")
st.write("The name on your Smoothie will be:", name_on_order)

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))

ingredients_list = st.multiselect(
    'Choose upto 5 ingredients:', my_dataframe 
)

if ingredients_list:

    # Join ingredients into a comma-separated string
    ingredients_string = ",".join(ingredients_list)

    # Build SQL correctly with 2 columns
    my_insert_stmt = f"""
        INSERT INTO smoothies.public.orders(ingredients, name_on_order)
        VALUES ('{ingredients_string}', '{name_on_order}')
    """

    st.write(my_insert_stmt)

    time_to_insert = st.button("Submit Order")

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")

  import requests
  smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
  st.text(smoothiefroot_response)


