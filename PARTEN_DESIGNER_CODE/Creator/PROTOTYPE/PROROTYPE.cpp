//prorotype dùng để sao chép bản gốc của lớp kế thừa mong muốn
//tạo 1 đối tượng mới sẽ mất nhiều thời gian và bộ nhớ hơn là sao chép 1 đối tượn đã tồn tại
#include "iostream"
#include "vector"
using namespace std;

class Stooge {
public:
   virtual Stooge* clone() = 0; //hàm để sao chép
   virtual void slap_stick() = 0; //hàm chức năng
};

//lớp dùng để sao chép
class Factory {
public:
   static Stooge* make_stooge( int choice );
private:
   static Stooge* s_prototypes[4];
};

//các lớp con triển khai Stooge
class Larry : public Stooge {
public:
   Stooge*   clone() { return new Larry; }
   void slap_stick() {
      cout << "Larry: poke eyes\n"; }
};
class Moe : public Stooge {
public:
   Stooge*   clone() { return new Moe; }
   void slap_stick() {
      cout << "Moe: slap head\n"; }
};
class Curly : public Stooge {
public:
   Stooge*   clone() { return new Curly; }
   void slap_stick() {
      cout << "Curly: suffer abuse\n"; }
};

//triển khai lớp factory
Stooge* Factory::s_prototypes[] = {
   new Larry, new Larry, new Moe, new Curly //
};
Stooge* Factory::make_stooge( int choice ) {
   return s_prototypes[choice]->clone();
}

int main() {
   Stooge *s0=Factory::make_stooge(0);
   Stooge *s1=Factory::make_stooge(1);
   Stooge *s2=Factory::make_stooge(2);
   Stooge *s3=Factory::make_stooge(3);
   s0->slap_stick();
   s1->slap_stick();
   s2->slap_stick();
   s3->slap_stick();
   return 1;
}

