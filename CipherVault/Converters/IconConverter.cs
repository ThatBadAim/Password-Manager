using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string iconName)
            {
                return iconName switch
                {
                    "Pencil" => "\xE70F", // Edit icon
                    "Eye" => "\xE890", // Reveal/Eye icon
                    "Copy" => "\xE8C8", // Copy icon
                    "Plus" => "\xE710", // Add icon
                    _ => "\xE716" // Default dot/bullet
                };
            }
            return "\xE716";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
