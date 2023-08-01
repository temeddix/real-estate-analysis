import streamlit as st
import aiohttp
import asyncio


# the callback function for the button will add 1 to the
# slider value up to 10
def plus_one():
    if st.session_state["slider"] < 10:
        st.session_state.slider += 1
    else:
        pass
    return


# when creating the button, assign the name of your callback
# function to the on_click parameter
add_one = st.button("Add one to the slider", on_click=plus_one, key="add_one")

# create the slider
slide_val = st.slider("Pick a number", 0, 10, key="slider")


async def sample_job():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org") as response:
            return await response.text()


async_output = asyncio.run(sample_job())
st.code(async_output[:1000], language="html")
