import streamlit as st

st.set_page_config(page_title="MiniStore", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main {
    padding: 2rem;
}
.product-card {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
    background-color: #f9f9f9;
}
.price {
    color: green;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Sample Products
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Noise-cancelling Bluetooth headphones.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Fitness tracking and notifications.",
        "category": "Electronics"
    },
    {
        "name": "Laptop Backpack",
        "price": 1499,
        "description": "Water-resistant backpack.",
        "category": "Accessories"
    },
    {
        "name": "Gaming Mouse",
        "price": 999,
        "description": "High precision RGB gaming mouse.",
        "category": "Electronics"
    },
    {
        "name": "Coffee Mug",
        "price": 399,
        "description": "Premium ceramic mug.",
        "category": "Home"
    },
    {
        "name": "Desk Lamp",
        "price": 1299,
        "description": "LED desk lamp with adjustable brightness.",
        "category": "Home"
    }
]

# Sidebar
st.sidebar.title("Categories")
categories = ["All"] + list(set([p["category"] for p in products]))
selected_category = st.sidebar.selectbox(
    "Select Category", categories
)

st.sidebar.title("Cart Summary")
st.sidebar.info("🛒 0 Items\n\nTotal: ₹0")

# Homepage
st.title("🛍️ MiniStore")
st.subheader("Welcome to MiniStore")
st.write("Discover amazing products at affordable prices.")

st.header("Featured Products")

filtered_products = products

if selected_category != "All":
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="product-card">
            <h3>{product['name']}</h3>
            <p>{product['description']}</p>
            <p><b>Category:</b> {product['category']}</p>
            <p class="price">₹{product['price']}</p>
        </div>
        """, unsafe_allow_html=True)