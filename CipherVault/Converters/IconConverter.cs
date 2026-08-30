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
                    "Eye" => "\uE890",    // ShowBcc
                    "Copy" => "\uE8C8",   // Copy
                    "Plus" => "\uE710",   // Add
                    _ => "\uE783"         // Error or Default Badge
                };
            }
            return "\uE783";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
