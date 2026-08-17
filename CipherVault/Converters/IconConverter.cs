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
                    "Pencil" => "\uE70F", // Edit
                    "Eye" => "\uE890",    // View
                    "Copy" => "\uE8C8",   // Copy
                    "Plus" => "\uE710",   // Add
                    "Shield" => "\uEA18",
                    "Calendar" => "\uE787",
                    "History" => "\uE81C",
                    _ => "\uE716"         // Placeholder (Dot or similar)
                };
            }
            return string.Empty;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
