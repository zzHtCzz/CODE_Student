#include "iostream"

#define window

using namespace std;

//các chưng năng chung giữa các nền tảng khác nhau
class widget
{
public:
    virtual void draw()=0;
};

//định nghĩa lại các tính năng dùng chức năng draw trên nền tảng 1
class linux_button:public widget
{
 public:
 void draw()
 {
    cout<<"linux button"<<endl;
 }
};

class linux_menu:public widget
{
 public:
 void draw()
 {
    cout<<"linux menu"<<endl;
 }
};

//định nghĩa lại các tính năng dùng chức năng draw trên nền tảng 2
class windown_button:public widget
{
 public:
 void draw()
 {
    cout<<"windown button"<<endl;
 }
};

class windown_menu:public widget
{
 public:
 void draw()
 {
    cout<<"windown menu"<<endl;
 }
};

//interface các tính năng
class factory
{
    public:
    virtual widget * create_button()=0;
    virtual widget * create_menu()=0;
};

//tính năng trên nền tảng 1, class này để truyền vào clien khi phát hiện ở nền tảng 1
class windown_factory:public factory
{
  widget *create_button()
  {
    return new windown_button;
  }
  widget *create_menu(){
    return new windown_menu;
  }
};
//tính năng trên nền tảng 2,class này để truyền vào clien khi phát hiện ở nền tảng 2
class linux_factory:public factory
{
  widget *create_button()
  {
    return new linux_button;
  }
  widget *create_menu(){
    return new linux_menu;
  }
};

//
class client
{
 private:
 factory *Factory;
 public:
 client(factory *f)
 {
  Factory=f;
 }

 void draw()
 {
    display1();
    display2();
 }

 void display1(){
     widget *w[]={
        Factory->create_button(),Factory->create_menu()
    };
    w[0]->draw();
    w[1]->draw();
 }

void display2(){
     widget *w[]={
        Factory->create_button(),Factory->create_menu()
    };
    w[0]->draw();
    w[1]->draw();
 }
};


int main()
{
    factory *Factory;
    #ifdef linux
    Factory=new linux_factory;
    #else
    Factory=new windown_factory;
    #endif

    client *c=new client(Factory);
    c->draw();
    return 0;
}

