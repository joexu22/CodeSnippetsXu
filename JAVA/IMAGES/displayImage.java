import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.io.File;

import javax.imageio.ImageIO;
import javax.swing.JFrame;

public class displayImage extends JFrame {

  private BufferedImage image;

  public static void main(String[] args) {
      new displayImage().setVisible(true);
  }

  public displayImage() {
    setDefaultCloseOperation(EXIT_ON_CLOSE);
    try {
      image = ImageIO.read(new File("sexy.png"));
    } catch (Exception e) {
      e.printStackTrace();
    }

    setSize(image.getWidth(), image.getHeight());
  }

  public void paint(Graphics g) {
    g.drawImage(image, 0, 0, getWidth(), getHeight(), this);
  }
}
