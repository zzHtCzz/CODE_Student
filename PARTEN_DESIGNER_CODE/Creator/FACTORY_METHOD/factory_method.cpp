//factory method

//cung cap interface de tao doi tuong trong lop cha nhung cho phep lop con thay doi loai doi tuong duoc tao
//uu diem: tra ve 1 gia tri nhieu lan
//tao 1 ham static de trra ve lop con mong muon


#include "iostream"
using namespace std;
class Creator //tao 1 interface
{
    public:
        static Creator * MakeCreator(int choice); //ham de tao lop con mong muon
        virtual void set_name_product(string name)=0;
        virtual void getname()=0;
       /* string getname() //trong interface khong duoc phep dinh nghia ham gi
        {
            printf("%s",name);
            return this->name;
        }
         Creator(string name){
            this->name=name;
         }
         ~Creator();*/
    protected:
    string name;
 
};

class sp1:public Creator
{
    void set_name_product(string name)
    {
        string str="sp1:";
        str+=name;
        this->name=str;
    }
    void getname()
    {
        cout<<name<<endl;
    }
};
class sp2:public Creator
{
    void set_name_product(string name)
    {
        string str="sp2:";
        str+=name;
        this->name=str;
    }
    void getname()
    {
       cout<<name<<endl;
    }
};
class sp3:public Creator
{
    void set_name_product(string name)
    {
         string str="sp3:";
        str+=name;
        this->name=str;
    }
    void getname()
    {
         cout<<name<<endl;
    }
};

Creator * Creator::MakeCreator(int choice)
{
    switch (choice)
    {
    case 0: return new sp1;
        break;
    case 1: return new sp2;
        break;
    case 2:return new sp3;
        break;
    default: return new sp1;
        break;
    }
}

int main()
{
 cout<<"hello \n";
 Creator *sp_1;
 Creator *sp_2;
 Creator *sp_3;
 sp_1=Creator::MakeCreator(0);
 sp_2=Creator::MakeCreator(1);
 sp_3=Creator::MakeCreator(2);
 sp_1->set_name_product("1");
 sp_2->set_name_product("2");
 sp_3->set_name_product("3");

 sp_1->getname();
 sp_2->getname();
 sp_3->getname();

 
 return 0;
}