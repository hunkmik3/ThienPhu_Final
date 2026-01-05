$products = @(
    @("kinh-cuong-luc", "Kính Cường Lực", "Kính cường lực có khả năng chịu lực gấp 4-5 lần kính thường, chịu sốc nhiệt tốt và đảm bảo an toàn tuyệt đối khi vỡ tạo thành các hạt nhỏ không sắc cạnh."),
    @("kinh-dan-an-toan", "Kính Dán An Toàn", "Gồm hai hay nhiều lớp kính ghép lại bằng lớp phim PVB, giúp kính không rơi ra khi vỡ, chống trộm và cách âm hiệu quả cho công trình."),
    @("kinh-hop", "Kính Hộp", "Cấu tạo bởi hai hay nhiều lớp kính ngăn cách bằng thanh đệm chứa hạt hút ẩm, mang lại khả năng cách âm và cách nhiệt vượt trội."),
    @("kinh-uon-cong", "Kính Uốn Cong", "Kính được gia nhiệt và uốn cong theo khuôn mẫu, tạo nên những đường cong mềm mại và kiến trúc độc đáo cho các công trình hiện đại."),
    @("kinh-nhung-mo-axit", "Kính Nhúng Mờ Axit", "Bề mặt kính được xử lý bằng hóa chất axit tạo độ mờ mịn, chống bám vân tay và mang lại vẻ đẹp sang trọng, riêng tư."),
    @("kinh-phun-cat-mo", "Kính Phun Cát Mờ", "Sử dụng công nghệ phun cát lên bề mặt để tạo độ nhám, có thể tạo các hoa văn trang trí nghệ thuật theo yêu cầu."),
    @("kinh-in-men", "Kính In Men", "Sử dụng mực gốm in lên kính và tôi nhiệt, tạo ra màu sắc và hình ảnh bền vĩnh cửu, không bong tróc hay phai màu."),
    @("kinh-phu-nano", "Kính Phủ Nano", "Lớp phủ Nano giúp bề mặt kính chống bám nước, bụi bẩn và dễ dàng vệ sinh, giữ cho kính luôn sáng bóng."),
    @("kinh-hoa-van", "Kính Hoa Văn", "Đa dạng mẫu mã như vân sọc, sóng, giọt nước, kim cương, vân mây... tạo điểm nhấn thẩm mỹ độc đáo cho không gian nội thất."),
    @("kinh-sieu-trong", "Kính Siêu Trong", "Loại bỏ tạp chất sắt giúp kính đạt độ trong suốt tối đa, truyền dẫn ánh sáng trung thực và tinh khiết."),
    @("kinh-phan-quang", "Kính Phản Quang", "Kính được phủ lớp oxit kim loại phản xạ ánh sáng, giảm nhiệt lượng và chói nắng. Các màu: xám, xanh biển, xanh lá..."),
    @("kinh-low-e", "Kính Low E", "Kính tiết kiệm năng lượng cao cấp, giảm thiểu tia cực tím và hồng ngoại nhưng vẫn giữ độ sáng. Màu sắc: trắng, xám, xanh..."),
    @("kinh-solar", "Kính Solar Control", "Dòng kính kiểm soát năng lượng mặt trời tối ưu, giảm chi phí điều hòa. Các màu: Neutral, Blue, Green, Gold..."),
    @("kinh-mau", "Kính Màu", "Kính được tạo màu trong quá trình sản xuất hoặc dán phim màu. Đa dạng sắc màu: xám, trà, xanh biển, đen..."),
    @("kinh-guong", "Kính Gương", "Kính tráng bạc cao cấp cho hình ảnh phản chiếu sắc nét. Các loại: gương trong, gương đen, xám, trà, giả cổ..."),
    @("kinh-dien", "Kính Điện (Smart Film)", "Công nghệ kính thông minh có thể chuyển đổi linh hoạt giữa trạng thái trong và mờ bằng dòng điện, mang lại sự riêng tư tức thì."),
    @("kinh-ghep-vai", "Kính Ghép Vải", "Sự kết hợp tinh tế giữa kính an toàn và các lớp vải nghệ thuật ở giữa, tạo nên vật liệu trang trí nội thất độc bản và đẳng cấp.")
)

New-Item -ItemType Directory -Force -Path "source/products" | Out-Null

foreach ($p in $products) {
    $slug = $p[0]
    $name = $p[1]
    $desc = $p[2]
    $filename = "source/products/$slug.html"
    
    $content = @"
@@include('header-product.htm')

@@include('blocks/navigation-product.htm')

<section class=""page-title bg-1"">
  <div class=""container"">
    <div class=""row"">
      <div class=""col-md-12"">
        <div class=""block text-center"">
          <span class=""text-white"">Chi tiết sản phẩm</span>
          <h1 class=""text-capitalize mb-4 text-lg"">$name</h1>
          <ul class=""list-inline"">
            <li class=""list-inline-item""><a href=""../index.html"" class=""text-white"">Trang Chủ</a></li>
            <li class=""list-inline-item""><span class=""text-white"">/</span></li>
            <li class=""list-inline-item""><a href=""../products.html"" class=""text-white"">Sản Phẩm</a></li>
            <li class=""list-inline-item""><span class=""text-white"">/</span></li>
            <li class=""list-inline-item""><a href=""#"" class=""text-white-50"">$name</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class=""section blog-details"">
    <div class=""container"">
        <div class=""row"">
            <div class=""col-lg-10 offset-lg-1"">
                <article class=""post"">
                    <div class=""post-image mb-5 text-center"">
                        <img loading=""lazy"" class=""img-fluid"" style=""max-height: 500px; width: auto;"" src=""../images/products/$slug.jpg"" alt=""$name"">
                    </div>
                    <div class=""post-content"">
                        <h3 class=""mb-3"">$name</h3>
                        <p class=""lead mb-4"">$desc</p>
                        
                        <div class=""alert alert-info"" role=""alert"">
                          <i class=""tf-ion-ios-information-outline mr-2""></i>
                          Thông tin chi tiết kỹ thuật, thông số và bảng giá cho sản phẩm <strong>$name</strong> đang được chúng tôi cập nhật. Vui lòng liên hệ trực tiếp qua Hotline để được tư vấn chính xác nhất.
                        </div>
                        
                        <div class=""mt-4"">
                             <a href=""../contact.html"" class=""btn btn-main"">Liên Hệ Báo Giá</a>
                        </div>
                    </div>
                </article>
            </div>
        </div>
        
        <div class=""row mt-5"">
            <div class=""col-12"">
                <div class=""title text-center"">
                    <h2>Sản Phẩm Khác</h2>
                    <div class=""border""></div>
                </div>
            </div>
            
            <div class=""col-lg-4 col-md-6 mb-4"">
                <div class=""product-item text-center"">
                     <div class=""product-image mb-3"">
                        <a href=""kinh-cuong-luc.html"">
                            <img loading=""lazy"" src=""../images/products/kinh-cuong-luc.jpg"" class=""img-fluid"" alt=""Kính Cường Lực"">
                        </a>
                    </div>
                     <h4><a href=""kinh-cuong-luc.html"">Kính Cường Lực</a></h4>
                </div>
            </div>
             <div class=""col-lg-4 col-md-6 mb-4"">
                <div class=""product-item text-center"">
                     <div class=""product-image mb-3"">
                        <a href=""kinh-dan-an-toan.html"">
                            <img loading=""lazy"" src=""../images/products/kinh-dan-an-toan.jpg"" class=""img-fluid"" alt=""Kính Dán An Toàn"">
                        </a>
                    </div>
                     <h4><a href=""kinh-dan-an-toan.html"">Kính Dán An Toàn</a></h4>
                </div>
            </div>
             <div class=""col-lg-4 col-md-6 mb-4"">
                <div class=""product-item text-center"">
                     <div class=""product-image mb-3"">
                        <a href=""kinh-hop.html"">
                            <img loading=""lazy"" src=""../images/products/kinh-hop.jpg"" class=""img-fluid"" alt=""Kính Hộp"">
                        </a>
                    </div>
                     <h4><a href=""kinh-hop.html"">Kính Hộp</a></h4>
                </div>
            </div>
        </div>
    </div>
</section>

@@include('footer-product.htm')
"@
    Set-Content -Path $filename -Value $content -Encoding UTF8
}
Write-Output "Done creating product files."
