import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.image.BufferedImage;
import java.io.IOException;
import javax.imageio.ImageIO;

interface ImageInterface {
    void displayImage();
}

class Image implements ImageInterface {
    private String filename;
    private boolean isLoaded;
    private BufferedImage imageData;

    public Image(String filename) {
        this.filename = filename;
        this.isLoaded = false;
        this.imageData = null;

        loadImageFromDisk();
    }

    private void loadImageFromDisk() {
        System.out.println("Loading " + filename + "...");
        try {
            imageData = ImageIO.read(getClass().getResource(filename));
            isLoaded = true;
        } catch (IOException e) {
            System.out.println("Error loading image: " + e.getMessage());
        }
    }

    public void displayImage() {
        if (!isLoaded) {
            loadImageFromDisk();
        }

        System.out.println("Displaying " + filename);
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new JLabel(new ImageIcon(imageData)));
        frame.pack();
        frame.setVisible(true);
    }
}

class ProxyImage implements ImageInterface {
    private String filename;
    private Image image;
    private boolean isLoaded;

    public ProxyImage(String filename) {
        this.filename = filename;
        this.image = null;
        this.isLoaded = false;
    }

    public void displayImage() {
        if (!isLoaded) {
            image = new Image(filename);
            isLoaded = true;
        }

        image.displayImage();
    }
}

class Usuario {
    private ImageInterface proxyImage;

    public Usuario(ImageInterface proxyImage) {
        this.proxyImage = proxyImage;
    }

    public void verImagen() {
        proxyImage.displayImage();
    }
}

public class ProxyExample {
    public static void main(String[] args) {
        ImageInterface proxyImage1 = new ProxyImage("imgs/UtnLogo.png");
        Usuario usuario1 = new Usuario(proxyImage1);
        usuario1.verImagen();

        ImageInterface proxyImage2 = new ProxyImage("imgs/ITI_Logo.png");
        Usuario usuario2 = new Usuario(proxyImage2);
        usuario2.verImagen();

        usuario1.verImagen();
    }
}