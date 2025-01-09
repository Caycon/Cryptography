# Introduct
- Ở đây mình sẽ trình bày 1 số trường hợp leak bits trong RSA thường gặp.
- Leak bits ở đây mình đề cập tới là một số trường hợp bits của private key bị leak 1 phần đủ để ta có thể sử dụng các kỹ thuật để ta có thể khôi phục lại từ đó decrypt được ciphertext.
- Tuy nhiên tùy vào trường hợp và độ dài của bits bị leak cũng như độ dài khóa được sử dụng mà thời gian recover key có thể mất khá nhiều thời gian.
## Demo
### Padding
#### Kịch bản
- Với case này **plaintext** đã được pad 1 số bytes vào. Tuy nhiên lại cho ta biết các bytes đó nằm ở vị trí như thế nào hoặc không (lúc này ta có thể brute force).
- Cụ thể thì case này cho ta giá trị của $c$, $n$, $e \ (small)$, $a$ (chuỗi được pad vào **plantext**), vị trí **plaintext** khi pad hoặc không:))).
#### Solution 