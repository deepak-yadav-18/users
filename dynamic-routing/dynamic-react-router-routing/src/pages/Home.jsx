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
            p={product}
          />
        ))}
      </div>
    </div>
  );
}

export default Home;

/*
Home.jsx ===> it shows all products arrays values => it creates number of ProductCard.jsx files according to product.js array size

ProductDetails.jsx => here we use useParams(to make routing dynamic through react-router-dom)



Home => ProductCard.jsx (show each product)
*/