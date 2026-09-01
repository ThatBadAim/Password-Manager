using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string iconType)
            {
                return iconType switch
                {
                    "Pencil" => "\uE70F", // Edit
                    "Eye" => "\uE890",    // View
                    "Copy" => "\uE8C8",   // Copy
                    "Plus" => "\uE710",   // Add
                    _ => "\uE716"         // Default (Info)
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
