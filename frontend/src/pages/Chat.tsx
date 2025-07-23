import { useState } from "react";

const Chart = () => {
    const [inputText, setInputText] = useState('');
    const [response, setResponse] = useState("");;

    const handleSend = async () => {
        const res = await fetch('http://localhost:8000/chat', {
            method: "POST",
            headers: {'Content-Type' : 'application/json'},
            body: JSON.stringify({
                user_id : 'text_user_0',
                input_text : inputText,
            })
        });

        const data = await res.json();
        setResponse(data.response);
    }
 
  return (
    <div style={{ padding: 20 }}>
      <h2>💬 AI 튜터와 대화</h2>

      <textarea
        rows={4}
        style={{ width: '100%' }}
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="무엇이든 물어보세요"
      />

      <div style={{ marginTop: 10 }}>
        <button onClick={handleSend}>보내기</button>
      </div>

      {response && (
        <div style={{ marginTop: 20, whiteSpace: 'pre-line' }}>
          <strong>GPT 응답:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
};

export default Chart;
