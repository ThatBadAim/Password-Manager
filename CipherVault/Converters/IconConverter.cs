using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            var iconName = value as string;
            return iconName switch
            {
                "Pencil" => "\uE70F", // Edit
                "Eye" => "\uE890", // Reveal
                "Copy" => "\uE8C8", // Copy
                "Plus" => "\uE710", // Add
                "Shield" => "\uEA18", // Shield
                "Calendar" => "\uE787", // Calendar
                "History" => "\uE81C", // History
                _ => "\uE774" // Globe as fallback
            };
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
