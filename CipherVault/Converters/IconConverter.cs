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
                    "Pencil" => "\xE70F", // Segoe MDL2 Edit
                    "Eye" => "\xE890",    // Segoe MDL2 View
                    "Copy" => "\xE8C8",   // Segoe MDL2 Copy
                    "Plus" => "\xE710",   // Segoe MDL2 Add
                    _ => "\xE716"         // Default generic dot or similar
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
