// src/pages/Home.jsx

import products from "../data/products.js";
import ProductCard from "../components/ProductCard.jsx";

function Home() {
  return (
    <div className="container">
      <h1>E-Commerce Store</h1>

      <div className="grid">
        {products.map((product) => (
          <ProductCard
            key={product.id}
            product={product}
          />
        ))}
      </div>
    </div>
  );
}

export default Home;