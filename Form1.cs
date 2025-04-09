using System;
using System.IO;
using System.Drawing;
using System.Diagnostics;
using System.Linq;
using System.Windows.Forms;

namespace ImageManagerApp
{
    public partial class Form1 : Form
    {
        string currentFolder = "";

        public Form1()
        {
            InitializeComponent();
        }

        private void btnBrowse_Click(object sender, EventArgs e)
        {
            using (FolderBrowserDialog dialog = new FolderBrowserDialog())
            {
                if (dialog.ShowDialog() == DialogResult.OK)
                {
                    currentFolder = dialog.SelectedPath;
                    LoadImages();
                }
            }
        }

        private void LoadImages()
        {
            lstImages.Items.Clear();
            picPreview.Image = null;

            string[] imageFiles = Directory.GetFiles(currentFolder, "*.*")
                .Where(file => file.EndsWith(".jpg", StringComparison.OrdinalIgnoreCase) ||
                               file.EndsWith(".png", StringComparison.OrdinalIgnoreCase) ||
                               file.EndsWith(".bmp", StringComparison.OrdinalIgnoreCase))
                .ToArray();

            foreach (var file in imageFiles)
                lstImages.Items.Add(Path.GetFileName(file));
        }

        private void lstImages_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (lstImages.SelectedItem == null) return;

            string selectedImagePath = Path.Combine(currentFolder, lstImages.SelectedItem.ToString());

            try
            {
                picPreview.Image = Image.FromFile(selectedImagePath);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error loading image: " + ex.Message);
            }
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            if (lstImages.SelectedItem == null) return;

            string path = Path.Combine(currentFolder, lstImages.SelectedItem.ToString());

            if (MessageBox.Show("Delete this image?", "Confirm", MessageBoxButtons.YesNo) == DialogResult.Yes)
            {
                File.Delete(path);
                LoadImages();
            }
        }

        private void btnOpen_Click(object sender, EventArgs e)
        {
            if (lstImages.SelectedItem == null) return;

            string path = Path.Combine(currentFolder, lstImages.SelectedItem.ToString());
            Process.Start(new ProcessStartInfo(path) { UseShellExecute = true });
        }
    }
}