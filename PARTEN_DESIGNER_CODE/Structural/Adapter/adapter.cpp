#include <iostream>
using namespace std;

// hàm triển khai hcn muốn sử dụng theo wh: service
class LegacyRectangle
{
  public:
    LegacyRectangle(int x1, int y1, int x2, int y2) //tọa độ
    {
        x1_ = x1;
        y1_ = y1;
        x2_ = x2;
        y2_ = y2;
        cout << "LegacyRectangle service:  create.  (" << x1_ << "," << y1_ << ") , ("
          << x2_ << "," << y2_ << ")" << endl;
    }
    void oldDraw()
    {
        cout << "LegacyRectangle:  oldDraw.  (" << x1_ << "," << y1_ << 
          ") => (" << x2_ << "," << y2_ << ")" << endl;
    }
  private:
    int x1_;
    int y1_;
    int x2_;
    int y2_;
};


// Desired interface
class Rectangle
{
  public:
    virtual void draw() = 0;
};
// Adapter để kết nối giữa rectange theo w,h và tọa độ
class RectangleAdapter: public Rectangle
{
    private: 
    LegacyRectangle *service_LegacyRectangle;
    public:
    RectangleAdapter(int x, int y, int w, int h)
    {
        cout << "RectangleAdapter: create.  (" << x << "," << y << 
          "), width = " << w << ", height = " << h << endl;

          service_LegacyRectangle=new LegacyRectangle(x,y,x+w,y+h); //chuyển đồi 2 tọa độ điểm sang 1 điểm gốc,w,h
    }
    void draw()
    {
        cout << "RectangleAdapter: draw." << endl;
       service_LegacyRectangle->oldDraw();
    }
};

int main()
{
  Rectangle *r = new RectangleAdapter(120, 200, 60, 40);
  r->draw();
}