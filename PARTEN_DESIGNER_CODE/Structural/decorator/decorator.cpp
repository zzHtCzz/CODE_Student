#include "iostream"
using namespace std;

//class ỉnterface component
class I {
  public:
    virtual ~I(){}
    virtual void do_it() = 0;
};

//class concreate component
class A: public I {
  public:
    ~A() {
        cout << "A dtor" << '\n';
    }
    /*virtual*/
    void do_it() {
        cout << 'A';
    }
};

//class base decorator, chú ý:   m_wrappee->do_it();
class D: public I {
  public:
    D(I *inner) {
        m_wrappee = inner;
    }
    ~D() {
        delete m_wrappee;
    }
    /*virtual*/
    void do_it() {
        m_wrappee->do_it();
    }
  private:
    I *m_wrappee;
};


//class concreate decoretor kế thừa base decorator và mở roognj thêm tính năng mới
class X: public D {
  public:
    X(I *core): D(core){} //constructor khi khwor tạo truyền core cho lớp con thì lớp cha cũng truyền vào cùng do : D(core)
    ~X() {
        cout << "X dtor" << "   ";
    }
    /*virtual*/
    void do_it() {
        D::do_it();
        cout << 'X';
    }
};

class Y: public D {
  public:
    Y(I *core): D(core){}
    ~Y() {
        cout << "Y dtor" << "   ";
    }
    /*virtual*/
    void do_it() {
        D::do_it();
        cout << 'Y';
    }
};

class Z: public D {
  public:
    Z(I *core): D(core){}
    ~Z() {
        cout << "Z dtor" << "   ";
    }
    /*virtual*/
    void do_it() {
        D::do_it();
        cout << 'Z';
    }
};

int main() { 
  I *anX = new X(new A);
  I *anXY = new Y(anX); //mở rộng y
  I *anXYZ = new Z(anXY);
  anX->do_it();
  cout << '\n';
  anXY->do_it();
  cout << '\n';
  anXYZ->do_it();
  cout << '\n';
  delete anX;
  delete anXY;
  delete anXYZ;
}