void main() {
  for (var i = 0; i < 10; i++) {
    String spaces = " " * (10 - i);
    String star = "*" * i;
    print(spaces + star);
  }

  String kata = 'MUKAMUKEK KONT';
  print(kata[1]);

  for (int i = 0; i < kata.length; i++) {
    var huruf = kata[i];
    if (huruf == ' ') {
      break;
    }
    print('Huruf saat ini: $huruf');
  }
}
