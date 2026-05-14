timeout=10,
            check=True,
        ) #hieuquan

        # Bước C: Thu thập log cuối cùng từ Receiver
        receiver_out, _ = receiver.communicate(timeout=10)

        # Bước D: Kiểm tra kết quả SENDER
        # (Lưu ý: Đảm bảo sender.py của ông có in các dòng này)
        assert "Key:" in sender_process.stdout
        assert "IV:" in sender_process.stdout
        # Nếu sender.py in tiếng Việt, hãy chỉnh lại chuỗi assert bên dưới
        assert "gửi" in sender_process.stdout.lower()

        # Bước E: Kiểm tra kết quả RECEIVER (Quan trọng nhất)
        assert "[+] Bản tin gốc:" in receiver_out
        assert test_message in receiver_out
        print("\n[OK] Test Roundtrip thành công! Tin nhắn đã đi từ Sender qua Receiver an toàn.")

    finally:
        # Đảm bảo tắt hẳn Receiver sau khi test xong hoặc nếu test fail
        if receiver.poll() is None:
            receiver.kill()
