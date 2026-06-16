// src/components/ProductCard.jsx

import { Link } from "react-router-dom";

function ProductCard({ p }) {
  return (
    <div className="card">
      <img src={p.image} alt={p.name} className="product-image" />
      <h3>{p.name}</h3>

      <p>{p.shortDescription}</p>

      <h4>₹{p.price}</h4>

      <Link to={`/product/${p.id}`}>
        <button>View Details</button>
      </Link>
    </div>
  );
}

export default ProductCard;
