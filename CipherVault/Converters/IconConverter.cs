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
                    "Pencil" => "\uE70F", // Edit icon
                    "Eye" => "\uE890",    // Reveal icon
                    "Copy" => "\uE8C8",   // Copy icon
                    "Plus" => "\uE710",   // Add icon
                    "Check" => "\uE73E",
                    "Shield" => "\uEA18",
                    "Calendar" => "\uE787",
                    "History" => "\uE81C",
                    "Link" => "\uE71B",
                    _ => "\uE716" // Default dot or placeholder
                };
            }
            return "\uE716";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
