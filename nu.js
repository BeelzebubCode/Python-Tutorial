// ค้นหา input radio ทั้งหมดที่มีค่า value="1"
document.querySelectorAll('input[type="radio"][value="1"]').forEach(radio => {
    radio.checked = true;
});

console.log("เลือกตัวเลือกที่มีค่า 1 ทั้งหมดแล้ว ✅");

console.log(document.querySelectorAll('input[type="radio"]'));