// src/components/MessageGenerator.jsx
import { useState } from 'react';
import axios from 'axios';

export default function MessageGenerator() {
  const [product, setProduct] = useState('');
  const [message, setMessage] = useState('');

  const generate = async () => {
    const res = await axios.post('http://localhost:5000/recommend', {
      product: product,
      tone: '친근하게',
    });
    setMessage(res.data.recommended_message);
  };

  return (
    <div className="message-box">
      <input
        type="text"
        value={product}
        onChange={(e) => setProduct(e.target.value)}
        placeholder="제품명을 입력하세요"
      />
      <button onClick={generate}>문구 생성</button>
      <p>{message}</p>
    </div>
  );
}
