# Hướng dẫn Deploy lên Vercel

## Cách 1: Deploy qua GitHub (Khuyến nghị)

1. **Đảm bảo code đã được push lên GitHub**
   - Code đã được push lên: https://github.com/hunkmik3/ThienPhu_Final

2. **Truy cập Vercel**
   - Vào https://vercel.com
   - Đăng nhập bằng tài khoản GitHub

3. **Import Project**
   - Click "Add New..." → "Project"
   - Chọn repository `hunkmik3/ThienPhu_Final`
   - Vercel sẽ tự động nhận cấu hình từ file `vercel.json`

4. **Cấu hình Deploy** (nếu cần)
   - Framework Preset: **Other**
   - Root Directory: `./` (mặc định)
   - Build Command: `npm run build` (tự động từ vercel.json)
   - Output Directory: `theme` (tự động từ vercel.json)
   - Install Command: `npm install` (tự động)

5. **Deploy**
   - Click "Deploy"
   - Chờ quá trình build hoàn tất
   - Website sẽ được deploy tại URL: `https://your-project-name.vercel.app`

## Cách 2: Deploy bằng Vercel CLI

### Bước 1: Cài đặt Vercel CLI
```bash
npm install -g vercel
```

### Bước 2: Đăng nhập Vercel
```bash
vercel login
```

### Bước 3: Deploy
```bash
cd F0_Tech_Website-main
vercel
```

### Bước 4: Deploy Production
```bash
vercel --prod
```

## Cấu hình đã được thiết lập

File `vercel.json` đã được tạo với các cấu hình:
- **Build Command**: `npm run build` (chạy gulp build)
- **Output Directory**: `theme` (thư mục chứa files đã build)
- **Install Command**: `npm install`

## Lưu ý

1. **Node.js Version**: Vercel sẽ tự động sử dụng Node.js phiên bản mới nhất
2. **Build Time**: Quá trình build có thể mất 2-5 phút
3. **Custom Domain**: Sau khi deploy, bạn có thể thêm custom domain trong Vercel Dashboard
4. **Environment Variables**: Nếu cần, có thể thêm trong Vercel Dashboard → Settings → Environment Variables

## Troubleshooting

### Lỗi Build
- Kiểm tra `package.json` có đầy đủ dependencies
- Đảm bảo Node.js version tương thích
- Xem logs trong Vercel Dashboard để debug

### Lỗi 404
- Kiểm tra file `vercel.json` có đúng cấu hình rewrites
- Đảm bảo output directory là `theme`

## Liên kết hữu ích

- Vercel Dashboard: https://vercel.com/dashboard
- Vercel Documentation: https://vercel.com/docs
- GitHub Repository: https://github.com/hunkmik3/ThienPhu_Final

