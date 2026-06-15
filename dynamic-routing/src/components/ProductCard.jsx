// src/components/ProductCard.jsx

import { Link } from "react-router-dom";

function ProductCard({ product }) {
  return (
    <div className="card">
      <img src={product.image} alt={product.name} className="product-image" />
      <h3>{product.name}</h3>

      <p>{product.shortDescription}</p>

      <h4>₹{product.price}</h4>

      <Link to={`/product/${product.id}`}>
        <button>View Details</button>
      </Link>
    </div>
  );
}

export default ProductCard;
