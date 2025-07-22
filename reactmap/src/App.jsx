import React, { useState } from 'react';
import './App.css';

// --- 設定項目 ---
const GRID_SIZE = 16; // グリッドのサイズ（16x16）
const PIXEL_SIZE = 30; // 1ピクセルの大きさ（30px）
const INITIAL_COLOR = '#ffffff'; // 初期の色（白）
const DRAW_COLOR = '#000000'; // 描画する色（黒）
// ----------------

function App() {
  // グリッドの状態を管理する変数
  // Array(GRID_SIZE * GRID_SIZE).fill(INITIAL_COLOR) で、
  // 全てのピクセルを初期の色で埋めた配列を作成します。
  const [pixels, setPixels] = useState(
    Array(GRID_SIZE * GRID_SIZE).fill(INITIAL_COLOR)
  );

  // ピクセルがクリックされたときの処理
  const handlePixelClick = (index) => {
    // pixels配列のコピーを作成します
    const newPixels = [...pixels];
    // クリックされたピクセルの色を描画色に変更します
    newPixels[index] = DRAW_COLOR;
    // stateを更新して画面を再描画します
    setPixels(newPixels);
  };

  return (
    <div className="app-container">
      <h1>React ドット絵ツール</h1>
      <div
        className="pixel-grid"
        style={{
          display: 'grid',
          gridTemplateColumns: `repeat(${GRID_SIZE}, ${PIXEL_SIZE}px)`,
          gridTemplateRows: `repeat(${GRID_SIZE}, ${PIXEL_SIZE}px)`,
          width: `${GRID_SIZE * PIXEL_SIZE}px`,
        }}
      >
        {pixels.map((color, index) => (
          <div
            key={index}
            className="pixel"
            style={{ backgroundColor: color }}
            onClick={() => handlePixelClick(index)}
          />
        ))}
      </div>
    </div>
  );
}

export default App;