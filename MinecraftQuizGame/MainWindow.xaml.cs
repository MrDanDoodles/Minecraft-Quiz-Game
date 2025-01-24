using System.Diagnostics;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace MinecraftQuizGame
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();


            // - - - - - Creating Menu Animation - - - - - 
            //Creating Transform Group
            var transformGroup = new TransformGroup();

            //Creating RotateTransform
            var rotateTransform = new RotateTransform(-15.969);
            transformGroup.Children.Add(rotateTransform);

            //Creating ScaleTransform
            var scaleTransform = new ScaleTransform(1.0, 1.0);
            transformGroup.Children.Add(scaleTransform);

            //Setting yellowMenuText trasnforms
            yellowMenuText.RenderTransform = transformGroup;
            yellowMenuText.RenderTransformOrigin = new Point(0.5, 0.5);

            //Creating the Growing Animation
            var growAnimation = new DoubleAnimation
            {
                From = 1.0,
                To = 1.25,
                Duration = TimeSpan.FromSeconds(1),
                AutoReverse = true, //Makes object go back to original size
                RepeatBehavior = RepeatBehavior.Forever //Will always be a loop
            };

            //Applying the Animation to the yellowMenuText
            scaleTransform.BeginAnimation(ScaleTransform.ScaleXProperty, growAnimation);
            scaleTransform.BeginAnimation(ScaleTransform.ScaleYProperty, growAnimation);


            // - - - - - QUESTIONS BUTTON - - - - - 
            string pythonExecutable = "C:\\Users\\1211d\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe";
            string pythonFile = @"C:\Users\1211d\Desktop\Computer Science\Personal Projects\C#\Minecraft Quiz Game\Questions_JSON_Python\Questions\Questions\Main.py";

            //Creating ProccessStartInfo Object
            var psi = new ProcessStartInfo
            {
                FileName = pythonExecutable,
                Arguments = pythonFile,
                RedirectStandardOutput = true, // Redirect output
                RedirectStandardError = true,  // Redirect error output
                UseShellExecute = false,       // Required for redirecting
                CreateNoWindow = true          // Run in background without opening a console window
            };
        
        }
        // - - - - - FUNCTIONS - - - - - 
        private void PlayGameClick(object sender, RoutedEventArgs e)
        {
            GameScreen gameScreen = new GameScreen(); // Create a new instance of GameScreen
            gameScreen.Show();                        // Show the new window
            this.Close();                           // Close the current window
        }
    
    }

    


}