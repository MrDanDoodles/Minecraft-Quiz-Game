using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using System.Text.Json;
using System.IO;

namespace MinecraftQuizGame
{
    /// <summary>
    /// Interaction logic for GameScreen.xaml
    /// </summary>
    public partial class GameScreen : Window
    {
        // - - - - VARIABLES - - - - 
        const string gameQuestionsFileString = @"C:\Users\1211d\Desktop\Computer Science\Personal Projects\C#\Minecraft Quiz Game\Questions_JSON_Python\game_questions.json";
        static Dictionary<string, string> gameQuestions = new Dictionary<string, string>(); //Dict where all game questions will be held

        //Getting info from JSON

        public GameScreen()
        {
            InitializeComponent(); //Dont Move THIS

            // - - - - GAME QUESTIONS - - - - 
            //Getting info from JSON
            string jsonData = File.ReadAllText(gameQuestionsFileString);
            gameQuestions = JsonSerializer.Deserialize<Dictionary<string, string>>(jsonData);
        }

        // - - - - FUNCTIONS - - - - 
        static int getRandomNumber()
        {
            int questionCount = gameQuestions.Count();
            Random random = new Random();
            int number = random.Next(0, questionCount);
            return number;
        }
        static string getNewQuestionKey(int randomNum)
        {
            var question = gameQuestions.ElementAt(randomNum);
            return question.Key;
        }
        void getNewQuestion(object sender, RoutedEventArgs e)
        {
            string question = getNewQuestionKey(getRandomNumber());
            questionText.Text = question;
        }
    }
}
