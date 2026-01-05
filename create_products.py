import os

# Base product data (slug, name, short_desc, img_file, long_desc, features_list, applications_list, specs)

# Helper function to generate bullet list HTML
def create_list_html(items):
    return "\n".join([f"                            <li><i class='tf-ion-ios-arrow-right mr-2 text-primary'></i>{item}</li>" for item in items])

products_data = [
    {
        "slug": "kinh-cuong-luc",
        "name": "Kính Cường Lực",
        "short_desc": "Kính cường lực có khả năng chịu lực gấp 4-5 lần kính thường, chịu sốc nhiệt tốt và đảm bảo an toàn tuyệt đối.",
        "img_file": "kinhcuongluc.jpg",
        "long_desc": "Kính cường lực (Tempered Glass) là loại kính an toàn được sản xuất bằng công nghệ gia nhiệt ở nhiệt độ cao (khoảng 700°C) và làm lạnh đột ngột bằng luồng khí lạnh. Quá trình này tạo ra sức căng bề mặt, giúp kính có khả năng chịu lực va đập, chịu nhiệt và sốc nhiệt vượt trội so với kính thường. Đặc biệt, khi vỡ, kính cường lực sẽ vỡ vụn thành các hạt nhỏ như hạt ngô, không có cạnh sắc nhọn, giảm thiểu tối đa nguy cơ gây sát thương cho người sử dụng.",
        "features": [
            "<strong>Độ bền cực cao:</strong> Chịu lực va đập gấp 4-5 lần so với kính nổi thông thường cùng độ dày.",
            "<strong>An toàn tuyệt đối:</strong> Khi vỡ tạo thành các hạt nhỏ không sắc cạnh, an toàn cho người dùng.",
            "<strong>Chịu sốc nhiệt tốt:</strong> Có thể chịu được sự thay đổi nhiệt độ đột ngột lên đến 150°C (trong khi kính thường chỉ khoảng 50°C).",
            "<strong>Độ phẳng và độ trong suốt:</strong> Giữ nguyên độ truyền sáng và màu sắc của kính gốc.",
            "<strong>Cách âm, cách nhiệt:</strong> Giảm tiếng ồn và hạn chế truyền nhiệt hiệu quả."
        ],
        "applications": [
            "Cửa kính thủy lực, cửa trượt tự động, vách ngăn văn phòng, vách tắm kính.",
            "Lan can cầu thang, ban công kính, mái kính, sàn kính.",
            "Mặt dựng tòa nhà, showroom, trung tâm thương mại.",
            "Kính ốp bếp, mặt bàn, kệ kính trang trí nội thất."
        ]
    },
    {
        "slug": "kinh-dan-an-toan",
        "name": "Kính Dán An Toàn",
        "short_desc": "Kính dán an toàn gồm nhiều lớp kính ghép lại bằng phim PVB, không rơi vỡ, chống trộm và cách âm.",
        "img_file": "kinh-cuong-luc-2-lop-3.jpg",
        "long_desc": "Kính dán an toàn (Laminated Glass) được tạo thành bằng cách ghép hai hay nhiều lớp kính lại với nhau bằng một hoặc nhiều lớp phim PVB (Polyvinyl Butyral) hoặc EVA ở giữa. Dưới tác động của nhiệt và áp suất, các lớp kính và phim liên kết chặt chẽ với nhau. Ưu điểm lớn nhất của loại kính này là khi bị vỡ, các mảnh kính vẫn dính chặt vào lớp phim, không bị văng ra ngoài, giúp bảo vệ an toàn tuyệt đối cho người và tài sản, đồng thời ngăn chặn sự xâm nhập từ bên ngoài.",
        "features": [
            "<strong>Không rơi vỡ:</strong> Mảnh vỡ dính chặt vào phim PVB, không gây nguy hiểm.",
            "<strong>An ninh cao:</strong> Chống lại sự đột nhập, trộm cắp, chịu được va đập mạnh.",
            "<strong>Cách âm ưu việt:</strong> Lớp phim PVB có khả năng hấp thụ âm thanh, giảm tiếng ồn hiệu quả.",
            "<strong>Ngăn tia UV:</strong> Loại bỏ đến 99% tia cực tím độc hại, bảo vệ sức khỏe và nội thất.",
            "<strong>Đa dạng màu sắc:</strong> Có thể sử dụng các lớp phim màu để tạo hiệu ứng thẩm mỹ."
        ],
        "applications": [
            "Mái kính, giếng trời (nơi có nguy cơ kính vỡ rơi xuống).",
            "Sàn kính, bậc cầu thang kính.",
            "Cửa đi, cửa sổ các tòa nhà cao tầng, biệt thự.",
            "Vách kính chống đạn, kính bảo vệ tại ngân hàng, tiệm vàng.",
            "Kính xe hơi, tàu hỏa, tàu thủy."
        ]
    },
    {
        "slug": "kinh-hop",
        "name": "Kính Hộp (Insulated Glass)",
        "short_desc": "Kính hộp có khả năng cách âm, cách nhiệt siêu việt, tiết kiệm năng lượng tối đa cho công trình.",
        "img_file": "kinh-hop-an-toan.jpg",
        "long_desc": "Kính hộp (IGU - Insulating Glass Unit) là giải pháp tối ưu cho việc tiết kiệm năng lượng và cách âm. Sản phẩm được cấu tạo bởi hai hoặc nhiều lớp kính, được ngăn cách bởi thanh đệm nhôm (spacer) bên trong có chứa hạt hút ẩm. Khoảng không giữa các lớp kính được bơm khí trơ (như Argon) và được bịt kín hoàn toàn bằng các lớp keo chuyên dụng. Cấu trúc này tạo ra một rào cản nhiệt và âm thanh cực kỳ hiệu quả.",
        "features": [
            "<strong>Cách nhiệt siêu hạng:</strong> Giảm thiểu sự truyền nhiệt từ ngoài vào trong và ngược lại, tiết kiệm 30-50% chi phí điện năng cho điều hòa.",
            "<strong>Cách âm tuyệt vời:</strong> Giảm tiếng ồn đáng kể, tạo không gian yên tĩnh.",
            "<strong>Ngưng tụ sương:</strong> Ngăn chặn hiện tượng đọng sương bề mặt do chênh lệch nhiệt độ.",
            "<strong>An toàn:</strong> Có thể kết hợp với kính cường lực hoặc kính dán để tăng độ an toàn.",
            "<strong>Linh hoạt:</strong> Có thể tích hợp nan trang trí bên trong hộp kính để tăng thẩm mỹ."
        ],
        "applications": [
            "Cửa sổ, cửa đi, vách kính mặt dựng các tòa nhà cao ốc, văn phòng, khách sạn.",
            "Vách ngăn phòng thu âm, phòng họp cần sự yên tĩnh.",
            "Tủ lạnh công nghiệp, tủ trưng bày thực phẩm.",
            "Các công trình xanh, công trình yêu cầu tiêu chuẩn tiết kiệm năng lượng cao."
        ]
    },
     {
        "slug": "kinh-uon-cong",
        "name": "Kính Uốn Cong",
        "short_desc": "Kính được gia nhiệt và uốn cong theo khuôn mẫu, tạo đường nét mềm mại và kiến trúc độc đáo.",
        "img_file": "kinhuongcong.jpg",
        "long_desc": "Kính uốn cong (Curved Glass) là sản phẩm kính được gia nhiệt đến điểm hóa mềm, sau đó được uốn cong theo khuôn mẫu thiết kế sẵn và làm nguội nhanh (đối với kính cường lực cong) hoặc làm nguội chậm (đối với kính thường uốn cong). Công nghệ này cho phép tạo ra các tấm kính với bán kính cong đa dạng, đáp ứng các yêu cầu kiến trúc phức tạp, mang lại vẻ đẹp mềm mại, uyển chuyển và độc đáo cho công trình.",
        "features": [
            "<strong>Thẩm mỹ độc đáo:</strong> Tạo nên các đường cong mềm mại, phá cách trong kiến trúc.",
            "<strong>Đa dạng chủng loại:</strong> Có thể uốn cong kính cường lực, kính dán, kính hộp...",
            "<strong>Độ bền cao:</strong> Kính cường lực cong vẫn giữ được khả năng chịu lực tốt.",
            "<strong>Tầm nhìn mở rộng:</strong> Tạo cảm giác không gian rộng mở và liền mạch hơn."
        ],
        "applications": [
            "Mặt dựng tòa nhà cong, vách kính xoắn ốc.",
            "Lan can cầu thang xoắn, ban công cong.",
            "Mái vòm kính, giếng trời hình cầu.",
            "Vách ngăn phòng tắm kính uốn cong.",
            "Quầy lễ tân, tủ trưng bày sản phẩm hình cong."
        ]
    },
    {
        "slug": "kinh-nhung-mo-axit",
        "name": "Kính Nhúng Mờ Axit",
        "short_desc": "Bề mặt kính được xử lý axit tạo độ mờ mịn, chống bám vân tay, mang lại vẻ đẹp sang trọng.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Kính nhúng mờ axit (Acid Etched Glass) là loại kính được xử lý bề mặt bằng hóa chất axit hydrofluoric đặc biệt. Quá trình này ăn mòn nhẹ bề mặt kính, tạo ra một lớp mờ đều, mịn màng như lụa và có độ bền vĩnh viễn (không bị bong tróc hay phai màu như dán decal). Kính axit có khả năng khuếch tán ánh sáng tốt, làm dịu ánh nắng gắt nhưng vẫn đảm bảo độ sáng cho không gian, đồng thời mang lại sự riêng tư cần thiết.",
        "features": [
            "<strong>Bề mặt mịn màng:</strong> Cảm giác sờ mịn tay, không bám dấu vân tay (non-fingerprint).",
            "<strong>Độ bền vĩnh cửu:</strong> Lớp mờ không bị trầy xước, không phai màu theo thời gian.",
            "<strong>Dễ dàng vệ sinh:</strong> Bề mặt trơn nhẵn, ít bám bẩn.",
            "<strong>Thẩm mỹ cao:</strong> Mang lại vẻ đẹp hiện đại, tinh tế và sang trọng.",
            "<strong>Đa dạng độ mờ:</strong> Có thể điều chỉnh mức độ mờ tùy theo yêu cầu."
        ],
        "applications": [
            "Vách ngăn phòng tắm, cửa phòng vệ sinh.",
            "Vách ngăn văn phòng, vách kính nội thất cần sự riêng tư.",
            "Cánh tủ áo, tủ bếp, mặt bàn kính.",
            "Cửa đi, cửa sổ trang trí.",
            "Bảng viết kính (glassboard)."
        ]
    },
    {
        "slug": "kinh-phun-cat-mo",
        "name": "Kính Phun Cát Mờ",
        "short_desc": "Công nghệ phun cát tạo độ nhám và hoa văn trang trí nghệ thuật trên bề mặt kính.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Kính phun cát (Sandblasted Glass) được tạo ra bằng cách phun một luồng cát mịn ở áp suất cao lên bề mặt kính. Quá trình này làm xói mòn bề mặt, tạo ra độ nhám và màu trắng mờ đặc trưng. Ưu điểm nổi bật của công nghệ này là có thể tạo ra các hoa văn, họa tiết, logo, chữ viết cực kỳ chi tiết và phức tạp theo thiết kế riêng (custom design). Có thể phun cát mờ toàn phần hoặc phun theo market.",
        "features": [
            "<strong>Hoa văn linh hoạt:</strong> Có thể tạo bất kỳ hình ảnh, logo, họa tiết nào theo yêu cầu.",
            "<strong>Tạo sự riêng tư:</strong> Che khuất tầm nhìn nhưng vẫn cho ánh sáng đi qua.",
            "<strong>Độ bám dính tốt:</strong> Lớp mờ là sự biến đổi của chính bề mặt kính nên rất bền.",
            "<strong>Giá thành hợp lý:</strong> Chi phí thấp hơn so với kính khắc 3D hay kính in men."
        ],
        "applications": [
            "Vách kính có logo công ty, vách ngăn trang trí.",
            "Cửa kính văn phòng, cửa đi thông phòng.",
            "Ô thoáng, vách tắm kính có họa tiết.",
            "Tranh kính nghệ thuật trang trí phòng khách.",
            "Biển hiệu, biển chỉ dẫn bằng kính."
        ]
    },
    {
        "slug": "kinh-in-men",
        "name": "Kính In Men (Ceramic Fritted Glass)",
        "short_desc": "Mực gốm in lên kính và tôi nhiệt tạo ra hình ảnh bền vĩnh cửu, không bong tróc.",
        "img_file": "kinh-in-men.jpg",
        "long_desc": "Kính in men gốm (Ceramic Fritted/Printed Glass) sử dụng công nghệ in kỹ thuật số hoặc in lụa để phủ lớp mực gốm đặc biệt lên bề mặt kính. Sau đó, kính được đưa vào lò tôi nhiệt ở nhiệt độ cao. Quá trình này làm cho lớp mực gốm nóng chảy và 'chết' vào bề mặt kính, trở thành một phần của kính. Kết quả là lớp màu/hình ảnh có độ cứng, độ bóng và độ bền tương đương với chính tấm kính.",
        "features": [
            "<strong>Bền màu vĩnh viễn:</strong> Chống chịu mọi điều kiện thời tiết, không bong tróc, không phai màu, chống trầy xước.",
            "<strong>Màu sắc đa dạng:</strong> Có thể in bất kỳ màu sắc, hình ảnh, họa tiết phức tạp nào.",
            "<strong>Kiểm soát ánh sáng:</strong> Có thể điều chỉnh độ phủ mực để kiểm soát lượng ánh sáng xuyên qua.",
            "<strong>Thân thiện môi trường:</strong> Mực in men gốm không chứa chì và các chất độc hại.",
            "<strong>Tính năng an toàn:</strong> Kính sau khi in thường là kính cường lực hoặc bán cường lực."
        ],
        "applications": [
            "Mặt dựng tòa nhà (façade), kính ốp tường ngoại thất.",
            "Mái kính, lam chắn nắng trang trí.",
            "Kính ốp bếp, kính ốp tường nội thất.",
            "Vách ngăn trang trí, cửa kính có họa tiết.",
            "Biển quảng cáo, bảng hiệu ngoài trời."
        ]
    },
    {
        "slug": "kinh-phu-nano",
        "name": "Kính Phủ Nano",
        "short_desc": "Lớp phủ Nano giúp kính chống bám nước, bụi bẩn, tự làm sạch và luôn sáng bóng.",
        "img_file": "kinh-phu-nano.jpg",
        "long_desc": "Kính phủ Nano (Nano Coated Glass/Self-cleaning Glass) là loại kính được phủ một lớp dung dịch Nano siêu mỏng lên bề mặt. Lớp phủ này có tính chất 'kỵ nước' (hydrophobic) mạnh mẽ, tạo ra hiệu ứng lá sen. Nước mưa khi rơi vào kính sẽ vo tròn thành hạt và trôi đi nhanh chóng, cuốn theo bụi bẩn, giúp bề mặt kính luôn sạch sẽ. Ngoài ra, lớp Nano còn giúp bảo vệ kính khỏi sự ăn mòn của axit nước mưa, nước biển và sự bám dính của cặn canxi.",
        "features": [
            "<strong>Tự làm sạch:</strong> Giảm thiểu tần suất vệ sinh kính, tiết kiệm chi phí bảo trì.",
            "<strong>Chống bám nước:</strong> Đảm bảo tầm nhìn rõ ràng ngay cả khi trời mưa to.",
            "<strong>Chống bám bụi, vôi hóa:</strong> Hạn chế sự tích tụ của bụi bẩn và ố mốc.",
            "<strong>Chống ăn mòn:</strong> Bảo vệ kính trước tác động của môi trường khắc nghiệt (vùng ven biển).",
            "<strong>Chịu nhiệt, chống tia UV:</strong> Tăng độ bền cho kính."
        ],
        "applications": [
            "Vách tắm kính (cabin tắm) - ứng dụng phổ biến nhất để chống cặn canxi.",
            "Mái kính, giếng trời (những vị trí khó vệ sinh).",
            "Mặt dựng, cửa sổ các tòa nhà cao tầng.",
            "Kính xe hơi, gương chiếu hậu.",
            "Kính tàu biển."
        ]
    },
    {
        "slug": "kinh-hoa-van",
        "name": "Kính Hoa Văn (Patterned/Textured Glass)",
        "short_desc": "Kính được cán vân hoặc đúc hoa văn tạo điểm nhấn thẩm mỹ độc đáo cho nội thất.",
        "img_file": "kinh-in-hoa-van-mo-3.jpg",
        "long_desc": "Kính hoa văn (Patterned/Textured Glass) được sản xuất bằng phương pháp cán nóng (với trục lô có khắc hoa văn) hoặc đúc khuôn. Bề mặt kính có các họa tiết nổi hoặc chìm như vân sọc, ô ly, giọt nước, vân mây, kim cương... Loại kính này không chỉ có tác dụng trang trí mà còn giúp tán xạ ánh sáng, tạo hiệu ứng lung linh cho không gian và hạn chế tầm nhìn từ bên ngoài (nhưng vẫn lấy sáng tốt).",
        "features": [
            "<strong>Tính thẩm mỹ cao:</strong> Tạo điểm nhấn nghệ thuật, cổ điển hoặc hiện đại cho không gian.",
            "<strong>Đa dạng mẫu mã:</strong> Hàng trăm mẫu hoa văn khác nhau (kính sọc, kính gợn sóng, kính hạt mưa...).",
            "<strong>Lấy sáng, che tầm nhìn:</strong> Giúp không gian sáng sủa nhưng vẫn đảm bảo sự kín đáo.",
            "<strong>Có thể cường lực:</strong> Một số loại kính hoa văn có thể tôi cường lực để tăng độ an toàn."
        ],
        "applications": [
            "Cánh tủ bếp, tủ áo, tủ rượu (cánh kính khung nhôm).",
            "Vách ngăn phòng, cửa đi, cửa sổ.",
            "Vách tắm kính, cửa nhà vệ sinh.",
            "Đèn trang trí, chao đèn.",
            "Vách kính nghệ thuật tại sảnh, quầy bar."
        ]
    },
    {
        "slug": "kinh-sieu-trong",
        "name": "Kính Siêu Trong (Ultra Clear Glass)",
        "short_desc": "Loại bỏ tạp chất sắt, đạt độ trong suốt tối đa, truyền dẫn ánh sáng trung thực.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Kính siêu trong (còn gọi là kính Low-Iron) là loại kính cao cấp được loại bỏ tối đa các tạp chất sắt trong quá trình sản xuất. Nếu nhìn ở cạnh kính thường (kính nổi), ta sẽ thấy màu xanh lá cây đậm, nhưng với kính siêu trong, cạnh kính hầu như không màu hoặc màu xanh dương rất nhạt. Kính đạt độ xuyên sáng lên tới hơn 91%, phản chiếu màu sắc của vật thể một cách trung thực và tinh khiết nhất.",
        "features": [
            "<strong>Độ trong suốt tuyệt đối:</strong> Loại bỏ ánh xanh của kính thường, cho tầm nhìn trong vắt.",
            "<strong>Hiển thị màu sắc trung thực:</strong> Không làm sai lệch màu sắc của vật thể phía sau kính.",
            "<strong>Thẩm mỹ đẳng cấp:</strong> Mang lại vẻ đẹp sang trọng, tinh tế cho công trình.",
            "<strong>Độ truyền sáng cao:</strong> Tối ưu hóa ánh sáng tự nhiên cho không gian.",
            "<strong>Có thể gia công:</strong> Có thể cường lực, dán an toàn, sơn màu như kính thường."
        ],
        "applications": [
            "Tủ trưng bày trang sức, đá quý, bảo tàng (nơi cần hiển thị màu sắc chuẩn xác).",
            "Bể cá cảnh thủy sinh cao cấp.",
            "Mặt dựng showroom thời trang, nội thất cao cấp.",
            "Mặt bàn kính, kệ kính trang trí.",
            "Kính sơn màu (sơn lên kính siêu trong cho màu sắc chuẩn nhất)."
        ]
    },
    {
        "slug": "kinh-phan-quang",
        "name": "Kính Phản Quang (Reflective Glass)",
        "short_desc": "Kính phủ lớp oxit kim loại phản xạ ánh sáng, giảm nhiệt lượng và chói nắng.",
        "img_file": "kinh-phan-quang.jpg",
        "long_desc": "Kính phản quang là loại kính phẳng được phủ một lớp màng phản quang bằng oxit kim loại siêu mỏng trên bề mặt. Lớp phủ này có tác dụng phản xạ lại phần lớn ánh sáng mặt trời, ngăn chặn tia tử ngoại và giảm thiểu nhiệt lượng truyền vào bên trong tòa nhà. Kính có đặc điểm là nhìn từ ngoài vào như một tấm gương (ban ngày), đảm bảo sự riêng tư tối đa, trong khi nhìn từ trong ra vẫn rõ ràng.",
        "features": [
            "<strong>Cản nhiệt tốt:</strong> Giảm bức xạ nhiệt mặt trời, giữ cho không gian bên trong mát mẻ.",
            "<strong>Chống chói lóa:</strong> Ngăn chặn ánh sáng gắt, bảo vệ mắt.",
            "<strong>Ngăn tia UV:</strong> Bảo vệ sức khỏe và nội thất tránh bị bạc màu.",
            "<strong>Tính riêng tư:</strong> Thiết kế 'nhìn một chiều' (ban ngày bên ngoài không nhìn thấy bên trong).",
            "<strong>Đa dạng màu sắc:</strong> Xanh lá, xanh biển, xám, đen... tạo vẻ đẹp hiện đại cho mặt dựng."
        ],
        "applications": [
            "Mặt dựng (façade) các tòa nhà cao tầng, văn phòng.",
            "Cửa sổ, vách kính hướng tây chịu nắng gắt.",
            "Mái kính che nắng.",
            "Kết hợp làm kính hộp để tăng hiệu quả cách nhiệt."
        ]
    },
    {
        "slug": "kinh-low-e",
        "name": "Kính Low E",
        "short_desc": "Kính tiết kiệm năng lượng, giảm tia cực tím và hồng ngoại nhưng vẫn giữ độ sáng.",
        "img_file": "kinh-low-e.jpg",
        "long_desc": "Kính Low-E (Low Emissivity) là loại kính có hệ số phát xạ thấp. Kính được phủ một hệ thống nhiều lớp kim loại và oxit kim loại (trong đó có lớp bạc) trong môi trường chân không. Lớp phủ này hoạt động như một màng lọc thông minh: cho phép ánh sáng nhìn thấy đi qua nhưng chặn lại phần lớn tia hồng ngoại (gây nóng) và tia tử ngoại (gây hại). Đây là giải pháp hàng đầu cho các công trình xanh tiết kiệm năng lượng.",
        "features": [
            "<strong>Cách nhiệt vượt trội:</strong> Giữ nhiệt độ trong phòng ổn định (mùa hè mát, mùa đông ấm).",
            "<strong>Tiết kiệm năng lượng:</strong> Giảm tải cho hệ thống điều hòa và sưởi ấm.",
            "<strong>Truyền sáng tốt:</strong> Đảm bảo không gian luôn ngập tràn ánh sáng tự nhiên.",
            "<strong>Chống ngưng tụ:</strong> Hạn chế đọng sương trên bề mặt kính.",
            "<strong>Bảo vệ nội thất:</strong> Ngăn chặn tia UV làm hư hại đồ đạc."
        ],
        "applications": [
            "Các tòa nhà văn phòng, cao ốc hạng A.",
            "Biệt thự, nhà phố hiện đại.",
            "Bệnh viện, trường học, khách sạn cao cấp.",
            "Cửa kính hộp Low-E là tiêu chuẩn cho các công trình tiết kiệm năng lượng."
        ]
    },
     {
        "slug": "kinh-solar",
        "name": "Kính Solar Control",
        "short_desc": "Dòng kính kiểm soát năng lượng mặt trời tối ưu, giảm chi phí điều hòa.",
        "img_file": "kinh-hop-solar.png",
        "long_desc": "Kính Solar Control là dòng kính cản nhiệt cao cấp được phủ nhiều lớp kim loại bằng công nghệ phún xạ magnetron. Khác với kính Low-E, kính Solar Control có khả năng ngăn chặn nhiệt lượng từ mặt trời trực tiếp hiệu quả hơn mà không làm giảm quá nhiều độ truyền sáng. Đặc biệt, kính Solar Control có thể lắp đơn (không cần làm kính hộp) mà vẫn đảm bảo hiệu quả cản nhiệt, giúp tiết kiệm chi phí thi công.",
        "features": [
            "<strong>Cản nhiệt hiệu quả:</strong> Ngăn chặn tới 65-70% năng lượng nhiệt mặt trời.",
            "<strong>Tiết kiệm chi phí:</strong> Giảm chi phí điện năng làm mát.",
            "<strong>Linh hoạt trong gia công:</strong> Có thể cường lực, uốn cong, dán an toàn sau khi phủ (đối với dòng phủ cứng).",
            "<strong>Màu sắc đẹp:</strong> Có các màu sắc trung tính, hiện đại như Neutral, Green, Blue, Grey...",
            "<strong>Không bị lóa:</strong> Độ phản quang vừa phải, không gây ô nhiễm ánh sáng."
        ],
        "applications": [
            "Mặt dựng tòa nhà, chung cư cao cấp.",
            "Cửa sổ, cửa đi các hướng hứng nắng.",
            "Mái kính, nhà kính.",
            "Showroom ô tô, showroom nội thất."
        ]
    },
    {
        "slug": "kinh-mau",
        "name": "Kính Màu (Tinted / Painted Glass)",
        "short_desc": "Kính được tạo màu trong quá trình sản xuất hoặc sơn màu, đa dạng sắc màu lựa chọn.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Kính màu thiên phú bao gồm hai dòng chính: Kính màu từ phôi (Tinted Glass - được trộn oxit kim loại tạo màu ngay khi nấu thủy tinh) và Kính sơn màu (Painted/Spandrel Glass - kính được phun sơn chịu nhiệt lên bề mặt). Dòng sản phẩm này mang lại sự lựa chọn phong phú về màu sắc cho các nhà thiết kế nội ngoại thất, giúp công trình trở nên sinh động và cá tính hơn.",
        "features": [
            "<strong>Màu sắc phong phú:</strong> Hơn 100 mã màu sơn đa dạng (kim sa, trơn, nhũ...).",
            "<strong>Bền màu:</strong> Kính sơn chịu nhiệt (sơn kính ốp bếp) chịu được nhiệt độ cao và ẩm ướt, không bong tróc.",
            "<strong>Dễ vệ sinh:</strong> Bề mặt kính phẳng, trơn bóng, không bám dầu mỡ (thích hợp ốp bếp).",
            "<strong>Thẩm mỹ:</strong> Tạo cảm giác không gian rộng hơn, sạch sẽ và hiện đại."
        ],
        "applications": [
            "Kính ốp bếp (kính màu cường lực) - ứng dụng phổ biến nhất.",
            "Kính ốp tường trang trí phòng khách, quầy lễ tân.",
            "Bảng viết kính văn phòng.",
            "Mặt bàn kính, cánh tủ kính.",
            "Kính màu cản nhiệt cho cửa sổ (đối với kính màu phôi)."
        ]
    },
    {
        "slug": "kinh-guong",
        "name": "Kính Gương (Mirror)",
        "short_desc": "Kính tráng bạc cao cấp cho hình ảnh phản chiếu sắc nét, sâu và chân thực.",
        "img_file": "kinh-guong.jpg",
        "long_desc": "Kính gương (gương soi) là kính được tráng một lớp bạc mỏng và các lớp sơn bảo vệ ở mặt sau, tạo nên khả năng phản chiếu hình ảnh hoàn hảo. Thiên Phú cung cấp các loại gương cao cấp nhập khẩu (gương Bỉ AGC, gương Thái Lan...) và gương tráng bạc trong nước chất lượng cao. Gương không chỉ để soi mà còn là vật liệu 'mở rộng không gian' hiệu quả nhất trong thiết kế nội thất.",
        "features": [
            "<strong>Hình ảnh sắc nét:</strong> Phản chiếu trung thực, sáng rõ, không méo mó.",
            "<strong>Chống ố mốc:</strong> Gương tráng bạc cao cấp có khả năng chống oxy hóa tốt trong môi trường ẩm (phòng tắm).",
            "<strong>Đa dạng chủng loại:</strong> Gương tráng bạc (silver mirror), gương tráng đồng, gương xám khói, gương màu trà, gương giả cổ...",
            "<strong>Gia công tinh xảo:</strong> Mài vát cạnh, mà xiết, khắc CNC trên gương."
        ],
        "applications": [
            "Gương phòng tắm, gương bàn trang điểm.",
            "Gương ghép trang trí ốp tường (phòng khách, phòng ăn).",
            "Gương phòng tập Gym, Yoga, múa.",
            "Trần gương, cột ốp gương.",
            "Gương trang trí sảnh khách sạn, thang máy."
        ]
    },
    {
        "slug": "kinh-dien",
        "name": "Kính Điện Thông Minh (Smart Film Glass)",
        "short_desc": "Kính chuyển đổi trạng thái trong-mờ tức thì bằng điện, mang lại sự riêng tư hiện đại.",
        "img_file": "kinhcuongluc.jpg", # Placeholder
        "long_desc": "Kính điện thông minh (Smart Glass / Switchable Glass) là sản phẩm công nghệ cao, hoạt động dựa trên nguyên lý điện tích hợp các tinh thể lỏng (PDLC) kẹp giữa hai lớp kính. Khi có dòng điện đi qua, các tinh thể sắp xếp thẳng hàng cho phép ánh sáng đi qua (kính trong suốt). Khi ngắt điện, các tinh thể phân tán ngẫu nhiên chặn ánh sáng (kính chuyển sang màu trắng mờ đục). Người dùng có thể điều khiển qua công tắc, remote hoặc cảm biến.",
        "features": [
            "<strong>Riêng tư tức thì:</strong> Chuyển đổi trạng thái chỉ trong 0.1 giây.",
            "<strong>Màn chiếu khổng lồ:</strong> Khi ở trạng thái mờ, kính có thể dùng làm màn hình chiếu sau độ nét cao.",
            "<strong>Cách âm, cách nhiệt:</strong> Cấu tạo như kính dán an toàn nên có tính năng cách âm, cách nhiệt tốt.",
            "<strong>Hiện đại và đẳng cấp:</strong> Thay thế rèm cửa truyền thống, tạo không gian mở sang trọng.",
            "<strong>An toàn:</strong> Chịu lực tốt và giữ mảnh vỡ khi va đập."
        ],
        "applications": [
            "Vách ngăn phòng họp, phòng giám đốc, phòng chủ tịch.",
            "Vách kính phòng tắm khách sạn 5 sao, phòng ngủ master.",
            "Vách kính bệnh viện (phòng mổ, hồi sức), nha khoa.",
            "Cửa sổ máy bay, du thuyền.",
            "Vách ngăn quầy giao dịch ngân hàng."
        ]
    },
    {
        "slug": "kinh-ghep-vai",
        "name": "Kính Ghép Vải (Fabric Laminated Glass)",
        "short_desc": "Sự kết hợp tinh tế giữa kính an toàn và vải nghệ thuật, vật liệu nội thất độc bản.",
        "img_file": "kinh-ghep-vai.jpg",
        "long_desc": "Kính ghép vải là dòng kính dán an toàn cao cấp, trong đó lớp phim ở giữa được thay thế hoặc kết hợp với các chất liệu vải, lụa, sợi kim loại, lưới, giấy gạo... dưới sự bảo vệ của các lớp kính trong suốt. Sự kết hợp này mang lại vẻ đẹp mềm mại, họa tiết phong phú của vải đồng thời vẫn giữ được độ cứng, độ bóng và dễ vệ sinh của kính. Đây là vật liệu 'độc bản' mang tính cá nhân hóa cao cho các công trình.",
        "features": [
            "<strong>Thẩm mỹ độc đáo:</strong> Hàng ngàn mẫu vải, hoa văn để lựa chọn, không đụng hàng.",
            "<strong>An toàn:</strong> Có đầy đủ tính năng của kính dán an toàn (không rơi vỡ).",
            "<strong>Bảo vệ vật liệu lõi:</strong> Lớp vải được kẹp kín giữa hai lớp kính nên không bị bụi bẩn, ẩm mốc, phai màu.",
            "<strong>Ứng dụng đa dạng:</strong> Vừa là vật liệu xây dựng, vừa là tác phẩm nghệ thuật.",
            "<strong>Dễ vệ sinh:</strong> Chỉ cần lau chùi bề mặt kính, không cần giặt như rèm vải."
        ],
        "applications": [
            "Vách ngăn trang trí phòng khách, vách đầu giường ngủ.",
            "Cửa lùa, cửa đi thông phòng.",
            "Mặt bàn trà, mặt quầy bar.",
            "Vách tắm kính nghệ thuật.",
            "Trần kính xuyên sáng trang trí."
        ]
    }
]

if not os.path.exists("source/products"):
    os.makedirs("source/products")

for product in products_data:
    filename = f"source/products/{product['slug']}.html"
    
    features_html = create_list_html(product['features'])
    applications_html = create_list_html(product['applications'])
    
    content = f"""@@include('header-product.htm')

@@include('blocks/navigation-product.htm')

<section class="page-title bg-1">
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="block text-center">
          <span class="text-white">Chi tiết sản phẩm</span>
          <h1 class="text-capitalize mb-4 text-lg">{product['name']}</h1>
          <ul class="list-inline">
            <li class="list-inline-item"><a href="../index.html" class="text-white">Trang Chủ</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="../products.html" class="text-white">Sản Phẩm</a></li>
            <li class="list-inline-item"><span class="text-white">/</span></li>
            <li class="list-inline-item"><a href="#" class="text-white-50">{product['name']}</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section blog-details">
    <div class="container">
        <div class="row">
            <div class="col-lg-10 offset-lg-1">
                <article class="post">
                    <div class="post-image mb-5 text-center">
                        <img loading="lazy" class="img-fluid" style="max-height: 500px; width: auto;" src="../images/products/{product['img_file']}" alt="{product['name']}">
                    </div>
                    <div class="post-content">
                        <h3 class="mb-3">{product['name']}</h3>
                        
                        <div class="mb-5 text-justify" style="font-size: 1.1rem; color: #555;">
                            {product['long_desc']}
                        </div>

                        <div class="row mb-5 w-100 mx-0">
                            <div class="col-12 col-md-6 mb-4 mb-md-0">
                                <div class="p-4 bg-light rounded border">
                                    <h4 class="mb-4 text-dark"><i class="tf-ion-ios-star mr-2 text-warning"></i>Đặc Điểm Nổi Bật</h4>
                                    <ul class="list-unstyled">
                                        {features_html}
                                    </ul>
                                </div>
                            </div>
                            <div class="col-12 col-md-6">
                                <div class="p-4 bg-light rounded border">
                                    <h4 class="mb-4 text-dark"><i class="tf-ion-ios-lightbulb mr-2 text-warning"></i>Ứng Dụng</h4>
                                    <ul class="list-unstyled">
                                        {applications_html}
                                    </ul>
                                </div>
                            </div>
                        </div>

                        <div class="alert alert-success mt-4" role="alert">
                           <h5 class="alert-heading mb-2"><i class="tf-ion-ios-telephone mr-2"></i>Liên Hệ Tư Vấn & Báo Giá</h5>
                           <p class="mb-0">Quý khách hàng quan tâm đến sản phẩm <strong>{product['name']}</strong>, vui lòng liên hệ trực tiếp qua Hotline của Thiên Phú Glass để được tư vấn kích thước, giải pháp thi công và nhận báo giá ưu đãi nhất.</p>
                        </div>
                        
                        <div class="mt-4 text-center">
                             <a href="../contact.html" class="btn btn-main">Yêu Cầu Báo Giá</a>
                             <a href="tel:+84837923996" class="btn btn-solid-border ml-2">Gọi Ngay: 083.792.3996</a>
                        </div>
                    </div>
                </article>
            </div>
        </div>
        
        <div class="row mt-5">
            <div class="col-12">
                <div class="title text-center">
                    <h2>Sản Phẩm Khác</h2>
                    <div class="border"></div>
                </div>
            </div>
            
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="product-card">
                    <div class="product-card-image">
                        <img loading="lazy" src="../images/products/kinhcuongluc.jpg" alt="Kính Cường Lực">
                        <div class="overlay">
                            <a href="kinh-cuong-luc.html" class="btn-view">Xem Chi Tiết</a>
                        </div>
                    </div>
                    <div class="product-card-content">
                        <h4><a href="kinh-cuong-luc.html">Kính Cường Lực</a></h4>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="product-card">
                    <div class="product-card-image">
                        <img loading="lazy" src="../images/products/kinh-cuong-luc-2-lop-3.jpg" alt="Kính Dán An Toàn">
                        <div class="overlay">
                            <a href="kinh-dan-an-toan.html" class="btn-view">Xem Chi Tiết</a>
                        </div>
                    </div>
                    <div class="product-card-content">
                        <h4><a href="kinh-dan-an-toan.html">Kính Dán An Toàn</a></h4>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="product-card">
                    <div class="product-card-image">
                        <img loading="lazy" src="../images/products/kinh-hop-an-toan.jpg" alt="Kính Hộp">
                        <div class="overlay">
                            <a href="kinh-hop.html" class="btn-view">Xem Chi Tiết</a>
                        </div>
                    </div>
                    <div class="product-card-content">
                        <h4><a href="kinh-hop.html">Kính Hộp</a></h4>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

@@include('footer-product.htm')
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated Product Details Pages with Full Content")
