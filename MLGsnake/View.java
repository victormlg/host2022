import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class View {
    private Kontroll kontroll;
    JLabel[][] rutenett = new JLabel[12][12];
    private JLabel stillingen;
    Font defaultFont = new JLabel().getFont();

    public View(Kontroll kontroll) {
        try {
            UIManager.setLookAndFeel(
            UIManager.getCrossPlatformLookAndFeelClassName());
        } catch (Exception e) {
            System.exit(9);
        }
        JFrame vindu = new JFrame("Snake");
        vindu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new BorderLayout());
        vindu.add(panel);


        JPanel grid = new JPanel();
        grid.setLayout(new GridLayout(12,12));
        grid.setBackground(Color.BLACK);
        
        for (int i =0; i < rutenett.length; i++) { 
            for (int k =0; k < rutenett[i].length; k++) {
                JLabel label = new JLabel(".");
                rutenett[i][k] = label;
                label.setPreferredSize(new Dimension(30,30));
                label.setHorizontalAlignment(JLabel.CENTER);
                label.setVerticalAlignment(JLabel.CENTER);
                grid.add(label);
            }
        }
        
        panel.add(grid, BorderLayout.SOUTH);
        panel.setBackground(new Color(65,55,50));

        JPanel toppen = new JPanel();
        toppen.setLayout(new BorderLayout());
        toppen.setBackground(new Color(55,45,40));

        stillingen = new JLabel("Score: 0");
        stillingen.setForeground(new Color(200, 200, 70));
        toppen.add(stillingen, BorderLayout.WEST);
        

        JPanel knapper = new JPanel();
        class nyRetning implements ActionListener, KeyListener {
            private char retning;
            public nyRetning(char retning) {
                this.retning = retning;
            }
            @Override
            public void actionPerformed(ActionEvent e) {
                kontroll.nyRetning(retning);
            }
            @Override
            public void keyPressed(KeyEvent e) {
                int keyCode = e.getKeyCode();
                if (keyCode == KeyEvent.VK_UP) kontroll.nyRetning('n');
                if (keyCode == KeyEvent.VK_DOWN) kontroll.nyRetning('s');
                if (keyCode == KeyEvent.VK_LEFT) kontroll.nyRetning('v');
                if (keyCode == KeyEvent.VK_RIGHT) kontroll.nyRetning('o');
            };
            @Override
            public void keyReleased(KeyEvent e) {};
            @Override
            public void keyTyped(KeyEvent e) {};
        }
        knapper.setLayout(new BorderLayout());
        knapper.setBackground(new Color(65,55,50));

        JButton nord = new JButton("^");
        nord.setBackground(new Color(55,45,40));
        nord.setForeground(new Color(200, 200, 70));
        nord.addActionListener(new nyRetning('n'));
        nord.addKeyListener(new nyRetning('n'));
        knapper.add(nord, BorderLayout.NORTH);
        
        JButton syd = new JButton("v");
        syd.setBackground(new Color(55,45,40));
        syd.setForeground(new Color(200, 200, 70));
        syd.addActionListener(new nyRetning('s'));
        syd.addKeyListener(new nyRetning('s'));
        knapper.add(syd, BorderLayout.SOUTH);

        JButton oest = new JButton(">");
        oest.setBackground(new Color(55,45,40));
        oest.setForeground(new Color(200, 200, 70));
        oest.addActionListener(new nyRetning('o'));
        oest.addKeyListener(new nyRetning('o'));
        knapper.add(oest, BorderLayout.EAST);

        JButton vest = new JButton("<");
        vest.setBackground(new Color(55,45,40));
        vest.setForeground(new Color(200, 200, 70));
        vest.addActionListener(new nyRetning('v'));
        vest.addKeyListener(new nyRetning('v'));
        knapper.add(vest, BorderLayout.WEST);


        toppen.add(knapper, BorderLayout.CENTER);

        JButton close = new JButton("close");
        class Lukk implements ActionListener{

            @Override
            public void actionPerformed(ActionEvent e) {
                kontroll.lukkVindu();
            }
        }
        close.addActionListener(new Lukk());
        close.setBackground(new Color(55,45,40));
        close.setForeground(new Color(200, 200, 70));
        toppen.add(close, BorderLayout.EAST);

        panel.add(toppen, BorderLayout.NORTH);

        vindu.pack();
        vindu.setVisible(true);
    }
    public void setFarge(int rad, int kol) {
        rutenett[rad][kol].setText("O");
        rutenett[rad][kol].setForeground(new Color(70, 220, 70));
        rutenett[rad][kol].setBackground(new Color(70, 220, 70));
        rutenett[rad][kol].setOpaque(true);
    }
    public void reset(int rad, int kol) {
        rutenett[rad][kol].setText(".");
        rutenett[rad][kol].setForeground(Color.DARK_GRAY);
        rutenett[rad][kol].setBackground(Color.BLACK);
        rutenett[rad][kol].setOpaque(true);
        rutenett[rad][kol].setFont(defaultFont);
    }
    public void setFarge(int rad, int kol, String X) {
        rutenett[rad][kol].setText(X);
        rutenett[rad][kol].setForeground(Color.RED);
        rutenett[rad][kol].setFont(new Font(Font.SANS_SERIF, Font.BOLD, 30));
    }
    public String hentString(int rad, int kol) {
        return rutenett[rad][kol].getText();
    }
    public void setScore(int tall) {
        stillingen.setText("Score: "+tall);
    }
    public void tapt() {
        stillingen.setForeground(new Color(255, 100, 80));
    }
}
