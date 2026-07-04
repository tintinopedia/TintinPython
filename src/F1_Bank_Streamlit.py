import streamlit as st

st.title("F1 Bank 🏎️")

tab1, tab2 = st.tabs(["🏦 Bank", "💼 Business"])

# ---- BANK TAB ----
with tab1:
    st.subheader("Welcome to the Bank!!")

    name = st.text_input("Enter your name:")

    if name:
        extra_money = 10000000
        st.write(f"Hello {name}!!")
        st.write(f"Your extra money is {extra_money} 💴")
        st.write("You can buy anything from your money which is given to you.")

        buy = st.radio("What do you want to buy?", ["Tyres", "New Car"])

        if buy == "Tyres":
            st.write("You chose Tyres. 🛞")
            tyre = st.radio("What kind of tyre?", ["Soft (4999)", "Medium (3246)", "Hard (2186)"])
            if st.button("Confirm Purchase"):
                if "Soft" in tyre:
                    cost = 4999
                elif "Medium" in tyre:
                    cost = 3246
                else:
                    cost = 2186
                left_money = extra_money - cost
                st.success(f"You chose {tyre}!")
                st.write(f"You have {left_money} left.")

        elif buy == "New Car":
            st.write("You chose New Car. 🛻")
            car = st.radio("Which car?", ["Ferrari 🏎️ (961410)", "Mercedes (599999)", "Redbull (600032)"])
            if st.button("Confirm Purchase"):
                if "Ferrari" in car:
                    cost = 961410
                elif "Mercedes" in car:
                    cost = 599999
                else:
                    cost = 600032
                left_money = extra_money - cost
                st.success(f"You chose {car}!")
                st.write(f"You have {left_money} left.")

# ---- BUSINESS TAB ----
with tab2:
    st.subheader("Welcome to the Business Section!!")

    if "earned_money" not in st.session_state:
        st.session_state.earned_money = 0

    with st.form("sell_form"):
        sell = st.text_input("What do you want to sell?")
        price = st.number_input("How much do you want to sell it for?", min_value=0, step=1)
        qty = st.number_input("How many do you want to sell?", min_value=1, step=1)
        submitted = st.form_submit_button("Sell")

    if submitted and sell:
        total = int(qty) * int(price)
        st.session_state.earned_money += total
        st.write(f"You sold {sell} for {total}")
        st.write(f"Total earned so far: {st.session_state.earned_money} 💴")

    if st.session_state.earned_money > 0:
        if st.button("Done selling"):
            st.write("Thanks for doing business with us!!")
            st.write("Thank you for your interest. 👋")
            st.session_state.earned_money = 0
