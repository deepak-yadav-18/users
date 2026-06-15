// src/pages/ProductDetails.jsx

import { useParams, Link } from "react-router-dom";
import products from "../data/products";

function ProductDetails() {
  const { id } = useParams();

  const product = products.find((item) => item.id === Number(id));

  if (!product) {
    return <h2>Product Not Found</h2>;
  }

  return (
    <div className="details">
      <img src={product.image} alt={product.name} className="product-image" />
      <h1>{product.name}</h1>

      <h2>₹{product.price}</h2>

      <p>{product.shortDescription}</p>

      <p>
        This is a detailed description page generated using React Dynamic
        Routing.
      </p>

      <Link to="/">
        <button>Back to Products</button>
      </Link>
    </div>
  );
}

export default ProductDetails;
